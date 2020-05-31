from shared.models import BaseAppModel
from cornerapps.user.models.shared import ProfileBaseModel


class UserProfileEmployee(BaseAppModel, ProfileBaseModel):

    class Meta(BaseAppModel.Meta):
        db_table = 'user_profile_employees'
