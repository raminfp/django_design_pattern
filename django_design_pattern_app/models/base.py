from django.utils import timezone
from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        """
        Override the default `save` method to update `updated_at` with the current
        time whenever the object is saved.

        :param args: Positional arguments to be passed to the `save` method.
        :param kwargs: Keyword arguments to be passed to the `save` method.
        """
        if self.pk:
            self.updated_at = timezone.now()
        super().save(*args, **kwargs)
