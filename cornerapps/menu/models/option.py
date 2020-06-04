from django.db import models
from shared.models import BaseAppModel
from cornerapps.menu.models import Menu


class Option(BaseAppModel):

    menu = models.ForeignKey(
        Menu,
        on_delete=models.CASCADE,
        related_name='options'
    )
    description = models.CharField(max_length=250)
