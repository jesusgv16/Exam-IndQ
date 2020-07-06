from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

from .managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    gender= models.CharField(max_length=1, choices=[('M','Male'),('F','Female')])

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'gender']

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj = None):
        return True
    def has_module_perms(self, app_label):
        return True



