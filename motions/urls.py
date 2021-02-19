from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from motions.views import MotionViewSet, MotionCategoryViewSet, MotionDifficultyViewSet, DebateFormatViewSet, \
    MotionAgeRangeViewSet, MotionTypeViewSet, MotionTrainingFocusViewSet, MotionImproPrepViewSet, MotionInfoTextViewSet, \
    MotionLinkViewSet, MotionCommentViewSet

app_name = 'motions'

router = DefaultRouter()
router.register(r'categories', MotionCategoryViewSet, basename='MotionCategory')
router.register(r'difficulties', MotionDifficultyViewSet, basename='MotionDifficulty')
router.register(r'debate-formats', DebateFormatViewSet, basename='DebateFormat')
router.register(r'age-ranges', MotionAgeRangeViewSet, basename='MotionAgeRange')
router.register(r'types', MotionTypeViewSet, basename='MotionType')
router.register(r'training-focuses', MotionTrainingFocusViewSet, basename='MotionTrainingFocus')
router.register(r'impro-prep', MotionImproPrepViewSet, basename='MotionImproPrep')
router.register(r'info-text', MotionInfoTextViewSet, basename='MotionInfoText')
router.register(r'links', MotionLinkViewSet, basename='MotionLink')
router.register(r'', MotionViewSet, basename='Motion')

urlpatterns = router.urls
