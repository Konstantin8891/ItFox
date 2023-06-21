from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models


from .managers import MyUserManager


class Users(AbstractBaseUser):

    ADMIN = 'admin'
    USER = 'user'

    ROLES = (
        (ADMIN, 'admin'),
        (USER, 'user'),
    )

    username = models.CharField(max_length=40, unique=True)
    password = models.CharField(max_length=100)
    role = models.CharField(max_length=5, choices=ROLES, default='user')

    objects = MyUserManager()

    USERNAME_FIELD = 'username'

    class Meta:
        verbose_name_plural = "Пользователи"

    def is_admin(self):
        return self.role == self.ADMIN

    @property
    def is_staff(self):
        return self.is_admin()

    @property
    def is_superuser(self):
        return self.is_admin()

    @property
    def is_active(self):
        return True

    def has_perm(self, perm, obj=None):
        return self.is_admin()

    def has_module_perms(self, app_label):
        return self.is_admin()

    def has_perms(self, perm_list, obj=None):
        return self.is_admin()
