# accounting/custom_user.py

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

class LegacyUserManager(BaseUserManager):
    # این متدها برای سازگاری لازم هستند اما ما از آنها استفاده نمی‌کنیم
    def create_user(self, *args, **kwargs):
        raise NotImplementedError("Legacy database does not support user creation.")

    def create_superuser(self, *args, **kwargs):
        raise NotImplementedError("Legacy database does not support superuser creation.")

class LegacyUser(AbstractBaseUser):
    # --- فیلدهای واقعی که در دیتابیس Users وجود دارند ---
    id = models.IntegerField(primary_key=True, db_column='Id')
    name = models.CharField(max_length=50, unique=True, db_column='Name')
    password = models.CharField(max_length=250, db_column='Pass', blank=True, null=True)
    is_active = models.BooleanField(default=True, db_column='Is_Active')
    semat = models.SmallIntegerField(db_column='Semat')

    # --- تنظیمات ضروری برای AbstractBaseUser ---
    USERNAME_FIELD = 'name'
    objects = LegacyUserManager()

    # --- ویژگی‌های (Properties) سفارشی ---
    @property
    def is_staff(self):
        return self.semat == 1

    @property
    def is_superuser(self):
        return self.semat == 1
    
    # --- متدهای ضروری برای سازگاری با ادمین جنگو ---
    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser
    
    # --- بازنویسی (Override) متدهای کلیدی ---
    def save(self, *args, **kwargs):
        """
        این متد را خالی می‌گذاریم تا جنگو هرگز تلاشی برای ذخیره این آبجکت
        (و به خصوص last_login) در دیتابیس legacy نکند.
        """
        pass

    def get_username(self):
        """متد get_username را برای سازگاری بیشتر بازنویسی می‌کنیم."""
        return self.name

    class Meta:
        managed = False
        db_table = 'Users'

    def __str__(self):
        return self.name

# --- تزریق (Monkey-patching) فیلد last_login ---
# این یک تکنیک پیشرفته است. ما به صورت دستی و فقط در زمان اجرا (runtime)
# یک ویژگی last_login به کلاس اضافه می‌کنیم تا جنگو را راضی کنیم،
# بدون اینکه این فیلد وارد منطق ORM شود.
LegacyUser.last_login = None 