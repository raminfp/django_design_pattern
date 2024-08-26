from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        abstract = True

