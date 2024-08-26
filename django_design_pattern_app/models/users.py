from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django_prometheus.models import ExportModelOperationsMixin
from django_design_pattern_app.models.base import BaseModel


class CustomUserManager(BaseUserManager):

    use_in_migrations = True

    def _create_user(self, username, password, **extra_fields):
        """Create and save a User with the given mobile and password."""

        if not username:
            raise ValueError('The given mobile must be set')

        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, password=None, **extra_fields):
        """Create and save a regular User with the given mobile and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, password, **extra_fields)

    def create_superuser(self, username, password, **extra_fields):
        """Create and save a SuperUser with the given mobile and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self._create_user(username=username, password=password, **extra_fields)


class Users(ExportModelOperationsMixin("representations"), AbstractUser, BaseModel):

    username = models.CharField(
        max_length=150, unique=True, null=True, blank=True, verbose_name="username", name="username")
    work_phone = models.CharField(
        max_length=20, null=True, blank=True, unique=True, verbose_name="work_phone", name="work_phone")
    address = models.CharField(
        max_length=20, null=True, verbose_name="address", name="address")
    is_active = models.BooleanField(
        default=False)
    city = models.CharField(
        max_length=100, null=True, blank=True, verbose_name="city", name="city")
    state = models.CharField(
        max_length=100, null=True, blank=True, verbose_name="state", name="state")
    is_new_user = models.BooleanField(default=False)
    agency_code = models.IntegerField()
    agency_name = models.CharField(max_length=254, blank=True, verbose_name="agency_name", name="agency_name")
    os_status = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    def __str__(self) -> str:
        return self.username

    def save(self, *args, **kwargs):
        # self.u_invitationCode = self.mobile
        super().save(*args, **kwargs)
