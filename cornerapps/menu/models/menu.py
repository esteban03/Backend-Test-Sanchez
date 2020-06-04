from django.db import models
from shared.models import BaseAppModel
from cornerapps.user.models import User


class Menu(BaseAppModel):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    day = models.DateField()

    class Meta(BaseAppModel.Meta):
        db_table = 'menus'
