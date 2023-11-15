from djoser.serializers import UserSerializer as BaseUserSerializer
from django.conf import settings
from users.models import User

class UserSerializer (BaseUserSerializer):
    class Meta (BaseUserSerializer.Meta):
        model = User
        fields = [
            'id',
            'username',
            'email',
            'phone',
            'is_superuser'
        ]