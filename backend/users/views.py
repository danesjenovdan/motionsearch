from django.shortcuts import render, get_object_or_404

from rest_framework import viewsets, status, permissions, authentication
from rest_framework.response import Response

from users.models import User, FavoriteMotion
from users.serializers import UserSerializer, UserFavoriteMotionSerializer
from motions.models import Motion


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('first_name', 'last_name')
    serializer_class = UserSerializer
    permission_classes=[permissions.IsAuthenticatedOrReadOnly,]

class UserFavoriteMotionsViewSet(viewsets.ModelViewSet):
    queryset = FavoriteMotion.objects.all().order_by('-created_at')
    serializer_class = UserFavoriteMotionSerializer
    lookup_field = 'user_pk'
    permission_classes=[permissions.IsAuthenticatedOrReadOnly,]

    def retrieve(self, request, *args, **kwargs):
        user = User.objects.get(pk=kwargs.get('user_pk', None))
        q = self.queryset.filter(user=user)
        return Response(data=self.serializer_class(q, many=True).data)
    def create(self, request, *args, **kwargs):
        motion = get_object_or_404(Motion, pk=request.data.get('motion', None))
        serializer = UserFavoriteMotionSerializer(data={"user": request.user.id, "motion": motion.id})
        if serializer.is_valid(raise_exception=False):
            serializer.save(user = request.user, motion = motion)
            return Response(serializer.data)


