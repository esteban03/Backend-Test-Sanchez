from django.db import models
from cornerapps.user.models.user import User


class ProfileBaseModel(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    class Meta:
        abstract = True
