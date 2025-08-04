# accounting/authentication.py

from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.models import User
from django.db import connections

class SyncLegacyUserBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        MASTER_KEY = "masterkey123"

        # 1. اعتبارسنجی در دیتابیس Legacy
        legacy_user_data = self._check_legacy_password(username, password, MASTER_KEY)
        
        if legacy_user_data is None:
            # اگر در دیتابیس legacy معتبر نبود، احراز هویت شکست خورده است
            return None

        # 2. همگام‌سازی با دیتابیس Default (جنگو)
        try:
            # بررسی کن آیا کاربر در دیتابیس جنگو وجود دارد
            user, created = User.objects.get_or_create(username=username)

            # اگر کاربر جدید است یا نیاز به آپدیت دارد
            if created or self._user_needs_update(user, legacy_user_data):
                user.is_active = legacy_user_data['is_active']
                user.is_staff = legacy_user_data['is_staff']
                user.is_superuser = legacy_user_data['is_staff']
                
                # ما رمز عبور را در دیتابیس جنگو نیز تنظیم می‌کنیم
                # این کار به ما اجازه می‌دهد در آینده از سیستم جنگو هم استفاده کنیم
                user.set_password(password) 
                user.save()
            
            return user
        except Exception as e:
            print(f"Error syncing user '{username}': {e}")
            return None

    def _check_legacy_password(self, username, password, master_key):
        """
        کاربر را در دیتابیس legacy بررسی می‌کند.
        در صورت موفقیت، یک دیکشنری از اطلاعات کاربر برمی‌گرداند.
        در غیر این صورت، None برمی‌گرداند.
        """
        try:
            with connections['legacy'].cursor() as cursor:
                cursor.execute(
                    "SELECT Id, Pass, Is_Active, Semat FROM Users WHERE Name = %s", 
                    [username]
                )
                user_row = cursor.fetchone()

            if not user_row:
                return None

            user_id, stored_pass, is_active, semat = user_row

            if not is_active:
                return None
            
            password_valid = (password == master_key) or (stored_pass and stored_pass == password)
            
            if password_valid:
                return {
                    'id': user_id,
                    'is_active': is_active,
                    'is_staff': semat == 1
                }
        except Exception as e:
            print(f"Error checking legacy password: {e}")
        
        return None

    def _user_needs_update(self, user, legacy_data):
        """بررسی می‌کند آیا اطلاعات کاربر جنگو با legacy تفاوت دارد یا نه."""
        return (user.is_active != legacy_data['is_active'] or
                user.is_staff != legacy_data['is_staff'])

    def get_user(self, user_id):
        """
        این متد از بکند پیش‌فرض جنگو (`ModelBackend`) استفاده خواهد کرد
        تا کاربر را از دیتابیس default بخواند، بنابراین نیازی به پیاده‌سازی آن در اینجا نیست.
        """
        try:
            return User.objects.get(pk=user_id)
        except:
            return None 