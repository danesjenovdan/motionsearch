from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter

from users.views import UserViewSet, UserFavoriteMotionsViewSet

app_name = 'users'

router = DefaultRouter()
router.register(r'', UserViewSet, basename='User')

urlpatterns = [
    url(r'^(?P<user_pk>\d+)/favorites/$', UserFavoriteMotionsViewSet.as_view({'get': 'retrieve', 'post':'create'}), name="user_favorites"),
    url(r'^oauth/', include(('oauth2_provider.urls', 'oauth'), namespace='oauth2_provider')),
]

urlpatterns += router.urls