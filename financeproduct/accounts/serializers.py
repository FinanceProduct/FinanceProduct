from dj_rest_auth.serializers import UserDetailsSerializer
from accounts.models import User

class CustomUserDetailsSerializer(UserDetailsSerializer):
    class Meta(UserDetailsSerializer.Meta):
        model = User
