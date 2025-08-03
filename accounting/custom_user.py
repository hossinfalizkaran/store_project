# accounting/custom_user.py

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from django.utils import timezone

class LegacyUserManager(BaseUserManager):
    def create_user(self, username, password=None):
        raise NotImplementedError("Cannot create users in a legacy database.")

    def create_superuser(self, username, password=None):
        raise NotImplementedError("Cannot create superusers in a legacy database.")

class LegacyUser(AbstractBaseUser):
    # فیلدهای واقعی که از دیتابیس خوانده می‌شوند
    id = models.IntegerField(primary_key=True, db_column='Id')
    name = models.CharField(max_length=50, unique=True, db_column='Name')
    password = models.CharField(max_length=250, db_column='Pass', blank=True, null=True)
    is_active = models.BooleanField(default=True, db_column='Is_Active')
    semat = models.SmallIntegerField(db_column='Semat')

    # ===> فیلد مجازی برای فریب دادن جنگو <===
    # این فیلد در دیتابیس وجود ندارد و هرگز ذخیره نخواهد شد.
    # ما فقط آن را در سطح مدل پایتون تعریف می‌کنیم.
    last_login = models.DateTimeField(blank=True, null=True)

    USERNAME_FIELD = 'name'
    REQUIRED_FIELDS = []

    objects = LegacyUserManager()

    @property
    def is_staff(self):
        return self.semat == 1

    @property
    def is_superuser(self):
        return self.semat == 1
    
    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser

    def get_username(self):
        return self.name

    def save(self, *args, **kwargs):
        # ===> بازنویسی متد save برای جلوگیری از نوشتن در دیتابیس <===
        # ما این متد را خالی می‌گذاریم تا جنگو هرگز تلاشی برای ذخیره
        # آبجکت LegacyUser (و فیلد last_login آن) نکند.
        # تمام عملیات نوشتن باید مستقیماً از طریق فرم‌ها و `using('legacy')` انجام شود.
        pass

    class Meta:
        managed = False
        db_table = 'Users'

    def __str__(self):
        return self.name 