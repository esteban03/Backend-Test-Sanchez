from django.contrib.auth.models import AbstractUser
from shared.models import BaseAppModel


class User(BaseAppModel, AbstractUser):

    class Meta(BaseAppModel.Meta):
        db_table = 'users'
