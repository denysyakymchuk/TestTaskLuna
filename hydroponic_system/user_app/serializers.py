from djoser.serializers import UserSerializer as BaseUserSerializer
from django.contrib.auth.models import User

from hydroponic_system_app.serializers import HydroponicSystemSerializer


class UserSerializer(BaseUserSerializer):
    hydroponic_system = HydroponicSystemSerializer(many=True, read_only=True)

    class Meta(BaseUserSerializer.Meta):
        model = User
        fields = BaseUserSerializer.Meta.fields + ('hydroponic_system',)
