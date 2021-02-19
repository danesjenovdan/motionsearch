from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.response import Response

from users.models import User, FavoriteMotion
from users.serializers import UserSerializer, UserFavoriteMotionSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('first_name', 'last_name')
    serializer_class = UserSerializer


class UserFavoriteMotionsViewSet(viewsets.ModelViewSet):
    queryset = FavoriteMotion.objects.all().order_by('-created_at')
    serializer_class = UserFavoriteMotionSerializer
    lookup_field = 'user_pk'

    def retrieve(self, request, *args, **kwargs):
        user = User.objects.get(pk=kwargs.get('user_pk', None))
        q = self.queryset.filter(user=user)
        return Response(data=self.serializer_class(q, many=True).data)

