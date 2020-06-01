from django.db import models
from shared.models import BaseAppModel
from cornerapps.menu.models import Option
from cornerapps.user.models import User


class Choose(BaseAppModel):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    option = models.ForeignKey(
        Option,
        on_delete=models.CASCADE
    )

    comments = models.CharField(max_length=250, blank=True, null=True)
