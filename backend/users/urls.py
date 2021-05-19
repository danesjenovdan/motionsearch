from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter

from users.views import UserViewSet, UserFavoriteMotionsViewSet, Me, MyFavorites, MyVotes, MyMotions

app_name = 'users'

router = DefaultRouter()
router.register(r'', UserViewSet, basename='User')

urlpatterns = [
    url(r'^me/$', Me.as_view({'get': 'retrieve'}), name="me"),
    url(r'^me/favorites$', MyFavorites.as_view({'get': 'retrieve'}), name="myFavorties"),
    url(r'^me/motions$', MyMotions.as_view({'get': 'retrieve'}), name="myMotions"),
    url(r'^me/votes$', MyVotes.as_view({'get': 'retrieve'}), name="myVotes"),
    url(r'^(?P<user_pk>\d+)/favorites/$', UserFavoriteMotionsViewSet.as_view({'get': 'retrieve', 'post':'create', 'delete': 'destroy'}), name="user_favorites"),
    url(r'^oauth/', include(('oauth2_provider.urls', 'oauth'), namespace='oauth2_provider')),
]

urlpatterns += router.urls