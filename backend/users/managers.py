from django.contrib.auth.models import BaseUserManager


class MyUserManager(BaseUserManager):
    def create_user(
            self,
            username,
            password=None
    ):
        user = self.model(
            username=username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(
            self,
            username,
            password=None
    ):
        user = self.create_user(
            password=password,
            username=username,
        )
        user.role = 'admin'
        user.save(using=self._db)
        return user
