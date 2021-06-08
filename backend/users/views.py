from django.core import paginator
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.contrib.auth.hashers import make_password
import six
from rest_framework import viewsets, status, permissions, authentication, views
from rest_framework.response import Response
from rest_framework.filters import OrderingFilter

from django_filters.rest_framework import DjangoFilterBackend, Filter, FilterSet

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.contrib.auth.models import User
from django.core.mail import EmailMessage

from django.core.paginator import Paginator

from users.models import User, FavoriteMotion
from users.serializers import UserSerializer, UserFavoriteMotionSerializer
from motions.models import Motion, MotionVote
from motions.serializers import MotionVoteSerializer, MotionSerializer

class TokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return (
            six.text_type(user.pk) + six.text_type(user.last_login) +
            six.text_type(user.is_active)
        )
account_activation_token = TokenGenerator()

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

class UsersFilterSet(FilterSet):
    id = MultiValueKeyFilter(field_name='id')
    username = MultiValueKeyFilter(field_name='username')
    email = MultiValueKeyFilter(field_name='email')
    class Meta:
        model = User
        fields = ('id', 'username', 'email')


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

class MyMotions(viewsets.ModelViewSet):
    queryset = Motion.objects.all().order_by('-created_at')
    serializer_class = MotionSerializer
    permission_classes=[permissions.IsAuthenticatedOrReadOnly,]
    filter_backends = (DjangoFilterBackend, OrderingFilter, )

    def retrieve(self, request, *args, **kwargs):
        q = self.queryset.filter(user=request.user.id)
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
    filter_backends = (DjangoFilterBackend,)
    filter_class = UsersFilterSet
    filter_fields = ('id', 'username', 'email')

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user = serializer.instance
        user.is_active = False
        user.save()
        mail_subject = 'Activate your account.'
        message = render_to_string('acc_active_email.html', {
            'user': user,
            'domain': 'motion-search-frontend-lb.djnd.si',
            'uid':urlsafe_base64_encode(force_bytes(user.pk)),
            'token':account_activation_token.make_token(user),
        })
        to_email = request.data.get('email', [])
        email = EmailMessage(
                    mail_subject, message, to=[to_email]
        )
        print("Email template was created. Trying to send email...")
        email.send()
        print("Email was succesfulyl sent.")
        return HttpResponse('Please confirm your email address to complete the registration')

    def activate(self, request, *args, **kwargs):
        try:
            uid = force_text(urlsafe_base64_decode(kwargs['uidb64']))
            user = User.objects.get(pk=uid)
        except(TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None
        if user is not None and account_activation_token.check_token(user, kwargs['token']):
            user.is_active = True
            user.save()
            login(request, user)
            # return redirect('home')
            return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
        else:
            return HttpResponse('Activation link is invalid!')

    def forgot(self, request, *args, **kwargs):
        user = User.objects.get(email=request.data.get('email', ''))
        mail_subject = 'Reset your account.'
        message = render_to_string('acc_reset_password.html', {
            'email': user,
            'domain': 'motion-search-frontend-lb.djnd.si',
            'uid':urlsafe_base64_encode(force_bytes(user.pk)),
            'token':account_activation_token.make_token(user),
        })
        to_email = request.data.get('email', [])
        email = EmailMessage(
                    mail_subject, message, to=[to_email]
        )
        print("Email template was created. Trying to send email...")
        email.send()
        print("Email was succesfulyl sent.")
        return HttpResponse('Check your email account for password change link')
    
    def changePassword(self, request, *args, **kwargs):
        try:
            uid = force_text(urlsafe_base64_decode(kwargs['uidb64']))
            user = User.objects.get(pk=uid)
        except(TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None
        if user is not None and account_activation_token.check_token(user, kwargs['token']):
            user.password = make_password(request.data.get('password', ''))
            user.save()
            return Response('Your password was updated succesfully, you can now login.')
        else:
            return Response('Password reset link is invalid!')
    

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

