from django.shortcuts import render, get_object_or_404

from rest_framework import viewsets, status, permissions, authentication
from rest_framework.response import Response

from django_filters.rest_framework import DjangoFilterBackend, Filter, FilterSet

from users.models import User, FavoriteMotion
from users.serializers import UserSerializer, UserFavoriteMotionSerializer
from motions.models import Motion, MotionVote
from motions.serializers import MotionVoteSerializer

class MultiValueKeyFilter(Filter):
    def filter(self, qs, value):
        if not value:
            return qs
        
        self.lookup_expr = 'in'
        values = value.split(',')
        return super(MultiValueKeyFilter, self).filter(qs, values)

class FavoritesFilterSet(FilterSet):
    id = MultiValueKeyFilter(field_name='id')
    user = MultiValueKeyFilter(field_name='user')
    motion = MultiValueKeyFilter(field_name='motion')
    class Meta:
        model = FavoriteMotion
        fields = ('id', 'user', 'motion')


class Me(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-created_at')
    serializer_class = UserSerializer
    def retrieve(self, request, *args, **kwargs):
        q = self.queryset.filter(pk=request.user.id)
        return Response(data=self.serializer_class(q, many=True).data)
class MyFavorites(viewsets.ModelViewSet):
    queryset = FavoriteMotion.objects.all().order_by('-created_at')
    serializer_class = UserFavoriteMotionSerializer
    lookup_field = 'user_pk'
    permission_classes=[permissions.IsAuthenticatedOrReadOnly,]
    filter_backends = (DjangoFilterBackend,)
    filter_class = FavoritesFilterSet
    filter_fields = ('id', 'user', 'motion')
    def retrieve(self, request, *args, **kwargs):
        user = User.objects.get(pk=request.user.id)
        q = self.queryset.filter(user=user)
        return Response(data=self.serializer_class(q, many=True).data)

class MyVotes(viewsets.ModelViewSet):
    queryset = MotionVote.objects.all().order_by('-created_at')
    serializer_class = MotionVoteSerializer
    def retrieve(self, request, *args, **kwargs):
        q = self.queryset.filter(user=request.user.id)
        return Response(data=self.serializer_class(q, many=True).data)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('first_name', 'last_name')
    serializer_class = UserSerializer


class UserFavoriteMotionsViewSet(viewsets.ModelViewSet):
    queryset = FavoriteMotion.objects.all().order_by('-created_at')
    serializer_class = UserFavoriteMotionSerializer
    lookup_field = 'user_pk'
    permission_classes=[permissions.IsAuthenticatedOrReadOnly,]
    filter_backends = (DjangoFilterBackend,)
    filter_class = FavoritesFilterSet
    filter_fields = ('id', 'user', 'motion')


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
    def destroy(self, request, *args, **kwargs):
        motion = get_object_or_404(Motion, pk=request.data.get('motion', None))
        favorite = FavoriteMotion.objects.get(user = request.user, motion = motion).delete()
        return Response(favorite)