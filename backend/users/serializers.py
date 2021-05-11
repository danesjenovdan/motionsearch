from rest_framework import serializers

from motions.serializers import MotionSerializer
from users.models import User, FavoriteMotion


class UserFavoriteMotionSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteMotion
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email')
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user