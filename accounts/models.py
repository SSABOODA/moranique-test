from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, email, name, password=None):
        if not email:
            raise ValueError('INVALID EMAIL')
        
        if not name:
            raise ValueError('INVALID NAME')
        
        user = self.model(
            email = self.normalize_email(email),
            name  = name,
        )

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password=None):
        user = self.create_user(
            email,
            name     = name,
            password = password,
        )

        user.id_admin = True
        user.save(using=self._db)

        return user

class User(AbstractBaseUser):
    email      = models.EmailField(default='', max_length=100, null=False, blank=False, unique=True)
    name       = models.CharField(default='', max_length=100, null=False, blank=False)
    is_activte = models.BooleanField(default=True) 
    is_admin   = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD  = 'email'


    class Meta:
        db_table = 'users'