from shared.models import BaseAppModel
from cornerapps.user.models.shared import ProfileBaseModel


class UserProfileChef(BaseAppModel, ProfileBaseModel):

    class Meta(BaseAppModel.Meta):
        db_table = 'user_profile_chefs'
