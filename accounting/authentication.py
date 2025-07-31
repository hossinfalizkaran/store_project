# accounting/authentication.py

from .models import LegacyUser

class LegacyDBBackend:
    def authenticate(self, request, username=None, password=None):
        MASTER_KEY = "masterkey123"

        try:
            # 1. تلاش برای پیدا کردن کاربر
            user = LegacyUser.objects.using('legacy').get(name=username)
            print(f"DEBUG: User '{username}' found in database.")

            # 2. بررسی فعال بودن کاربر
            if not user.is_active:
                print(f"DEBUG: Login failed. User '{username}' is not active.")
                return None

            # 3. بررسی Master Key
            if password == MASTER_KEY:
                print(f"DEBUG: Master Key login successful for user '{username}'.")
                return user

            # 4. بررسی رمز عبور واقعی
            print(f"DEBUG: Checking password for '{username}'. DB Pass: '{user.password}', Input Pass: '{password}'")
            if user.password and user.password == password:
                print(f"DEBUG: Regular password login successful for user '{username}'.")
                return user
            else:
                print(f"DEBUG: Login failed. Password mismatch for user '{username}'.")
                return None

        except LegacyUser.DoesNotExist:
            print(f"DEBUG: Login failed. User '{username}' does not exist.")
            return None
        except Exception as e:
            print(f"DEBUG: An unexpected error occurred in authenticate: {e}")
            return None
    
    def get_user(self, user_id):
        try:
            return LegacyUser.objects.using('legacy').get(pk=user_id)
        except LegacyUser.DoesNotExist:
            return None 