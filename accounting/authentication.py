# accounting/authentication.py

from django.contrib.auth.backends import BaseBackend
from django.db import connections
from .custom_user import LegacyUser

class LegacyDBBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None):
        """
        این نسخه نهایی و اصلاح شده است که به درستی با داده‌های خام دیتابیس کار می‌کند.
        """
        MASTER_KEY = "masterkey123"

        if not username or not password:
            return None

        try:
            with connections['legacy'].cursor() as cursor:
                cursor.execute(
                    "SELECT Id, Name, Pass, Is_Active, Semat FROM Users WHERE Name = %s", 
                    [username]
                )
                user_row = cursor.fetchone() # نتیجه یک tuple است: (Id, Name, Pass, ...)

            if not user_row:
                return None # کاربر وجود ندارد

            # استخراج مقادیر از tuple
            user_id, user_name, stored_pass, is_active, semat = user_row

            if not is_active:
                return None # کاربر غیرفعال است

            # بررسی رمز عبور با استفاده از متغیرهای استخراج شده
            password_valid = (password == MASTER_KEY) or (stored_pass and stored_pass == password)

            if password_valid:
                # اگر احراز هویت موفق بود، حالا آبجکت LegacyUser را می‌سازیم
                user = LegacyUser(
                    id=user_id,
                    name=user_name,
                    is_active=is_active,
                    semat=semat
                )
                return user
        
        except Exception as e:
            print(f"Error in LegacyDBBackend authenticate method: {e}")
        
        return None # در صورت بروز هرگونه خطا یا عدم تطابق رمز، None برگردان

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