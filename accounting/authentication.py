# accounting/authentication.py

from django.contrib.auth.backends import BaseBackend
from django.db import connections
from .custom_user import LegacyUser

class LegacyDBBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None):
        MASTER_KEY = "masterkey123"

        if not username or not password:
            print("DEBUG: Authenticate failed - username or password is missing.")
            return None

        try:
            with connections['legacy'].cursor() as cursor:
                cursor.execute(
                    "SELECT Id, Name, Pass, Is_Active, Semat FROM Users WHERE Name = %s", 
                    [username]
                )
                user_row = cursor.fetchone()

            if not user_row:
                print(f"DEBUG: Authenticate failed - User '{username}' not found in DB.")
                return None

            user_id, user_name, stored_pass, is_active, semat = user_row

            if not is_active:
                print(f"DEBUG: Authenticate failed - User '{username}' is not active.")
                return None

            print(f"DEBUG: Authenticating user '{username}'. Input Pass: '{password}'. Stored Pass: '{stored_pass}'")

            # بررسی Master Key
            if password == MASTER_KEY:
                print(f"DEBUG: Master Key MATCH for user '{username}'. Authentication successful.")
                user = LegacyUser(id=user_id, name=user_name, is_active=is_active, semat=semat)
                return user

            # بررسی رمز عبور واقعی
            if stored_pass and stored_pass == password:
                print(f"DEBUG: Regular password MATCH for user '{username}'. Authentication successful.")
                user = LegacyUser(id=user_id, name=user_name, is_active=is_active, semat=semat)
                return user
            
            print(f"DEBUG: Authenticate failed - Password MISMATCH for user '{username}'.")
            return None
        
        except Exception as e:
            print(f"ERROR in LegacyDBBackend authenticate method: {e}")
            return None

    def get_user(self, user_id):
        """
        این متد برای گرفتن کاربر از session استفاده می‌شود.
        به جای query کردن دیتابیس، مستقیماً از cursor استفاده می‌کنیم.
        """
        try:
            with connections['legacy'].cursor() as cursor:
                cursor.execute(
                    "SELECT Id, Name, Pass, Is_Active, Semat FROM Users WHERE Id = %s", 
                    [user_id]
                )
                user_row = cursor.fetchone()

            if not user_row:
                return None

            # استخراج مقادیر از tuple
            user_id, user_name, stored_pass, is_active, semat = user_row

            # ساخت آبجکت LegacyUser بدون query کردن ORM
            user = LegacyUser(
                id=user_id,
                name=user_name,
                password=stored_pass,
                is_active=is_active,
                semat=semat
            )
            return user

        except Exception as e:
            print(f"Error in LegacyDBBackend get_user method: {e}")
            return None 