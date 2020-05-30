from django.db import models


class BaseAppModel(models.Model):
    """
    Create all application models with this base model
    """

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
