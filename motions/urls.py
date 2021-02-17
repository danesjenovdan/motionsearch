from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from motions.views import MotionViewSet, MotionCategoryViewSet, MotionDifficultyViewSet, DebateFormatViewSet, \
    MotionAgeRangeViewSet

app_name = 'motions'

router = DefaultRouter()
router.register(r'category', MotionCategoryViewSet, basename='MotionCategory')
router.register(r'difficulty', MotionDifficultyViewSet, basename='MotionDifficulty')
router.register(r'debate-format', DebateFormatViewSet, basename='DebateFormat')
router.register(r'age-range', MotionAgeRangeViewSet, basename='MotionAgeRange')
router.register(r'', MotionViewSet, basename='Motion')

urlpatterns = router.urls
