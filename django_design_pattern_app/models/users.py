from django_prometheus.models import ExportModelOperationsMixin
from django_design_pattern_app.models.base import BaseModel
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

from django.contrib.auth.base_user import BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError('The Username field must be set')
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(username, password, **extra_fields)


class Users(ExportModelOperationsMixin("users"), AbstractUser, BaseModel):
    username = models.CharField(
        max_length=150, unique=True, null=True, blank=True, verbose_name="username", name="username"
    )
    password = models.CharField(max_length=128, null=True, blank=True)

    # groups = models.ManyToManyField(
    #     Group,
    #     related_name="custom_user_groups",
    #     blank=True,
    #     verbose_name="groups",
    #     help_text="The groups this user belongs to.",
    #     related_query_name="user",
    # )
    #
    # user_permissions = models.ManyToManyField(
    #     Permission,
    #     related_name="custom_user_permissions",
    #     blank=True,
    #     verbose_name="user permissions",
    #     help_text="Specific permissions for this user.",
    #     related_query_name="user",
    # )

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def __str__(self) -> str:
        """
        Return a string representation of this user.

        This string is the user's username.

        Returns:
            str: The user's username.
        """
        return self.username

