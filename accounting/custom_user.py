# accounting/custom_user.py

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

class LegacyUserManager(BaseUserManager):
    def create_user(self, username, password=None):
        raise NotImplementedError("Cannot create users in a legacy database.")

    def create_superuser(self, username, password=None):
        raise NotImplementedError("Cannot create superusers in a legacy database.")

class LegacyUser(AbstractBaseUser):
    id = models.IntegerField(primary_key=True, db_column='Id')
    name = models.CharField(max_length=50, unique=True, db_column='Name')
    password = models.CharField(max_length=250, db_column='Pass', blank=True, null=True)
    is_active = models.BooleanField(default=True, db_column='Is_Active')
    semat = models.SmallIntegerField(db_column='Semat')

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

    class Meta:
        managed = False
        db_table = 'Users'

    def __str__(self):
        return self.name 