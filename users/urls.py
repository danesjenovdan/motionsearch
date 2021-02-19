from django.conf.urls import url
from rest_framework.routers import DefaultRouter

from users.views import UserViewSet, UserFavoriteMotionsViewSet

app_name = 'users'

router = DefaultRouter()
router.register(r'', UserViewSet, basename='User')

urlpatterns = [
    url(r'^(?P<user_pk>\d+)/favorites/$', UserFavoriteMotionsViewSet.as_view({'get': 'retrieve'}), name="user_favorites"),
]

urlpatterns += router.urls
