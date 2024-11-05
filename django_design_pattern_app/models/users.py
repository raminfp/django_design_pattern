from django_prometheus.models import ExportModelOperationsMixin
from django_design_pattern_app.models.base import BaseModel
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models


class Users(ExportModelOperationsMixin("users"), AbstractUser, BaseModel):
    username = models.CharField(
        max_length=150, unique=True, null=True, blank=True, verbose_name="username", name="username"
    )
    password = models.CharField(max_length=128, null=True, blank=True)

    groups = models.ManyToManyField(
        Group,
        related_name="custom_user_groups",
        blank=True,
        verbose_name="groups",
        help_text="The groups this user belongs to.",
        related_query_name="user",
    )

    user_permissions = models.ManyToManyField(
        Permission,
        related_name="custom_user_permissions",
        blank=True,
        verbose_name="user permissions",
        help_text="Specific permissions for this user.",
        related_query_name="user",
    )

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def __str__(self) -> str:
        return self.username
