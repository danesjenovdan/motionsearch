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

    def create(self, validated_data):
        users_data = validated_data.pop('favorites')
        user = User.objects.create(**validated_data)
        favorites = []
        for user_data in users_data:
            favourite = MotionCategory.objects.create(user=user, **user_data)
            user.favorites.add(favourite)
        return user