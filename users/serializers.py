from rest_framework import serializers

from motions.serializers import MotionSerializer
from users.models import User, FavoriteMotion


class UserFavoriteMotionSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteMotion
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    favorites = MotionSerializer(many=True)

    class Meta:
        model = User
        fields = '__all__'
