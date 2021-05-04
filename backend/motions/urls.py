from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from motions.views import MotionViewSet, MotionCategoryViewSet, MotionDifficultyViewSet, DebateFormatViewSet, \
    MotionAgeRangeViewSet, MotionTypeViewSet, MotionTrainingFocusViewSet, MotionImproPrepViewSet, MotionInfoTextViewSet, \
    MotionLinkViewSet, MotionCommentViewSet, MotionWhereUsedViewSet, MotionVoteViewSet

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
router.register(r'where-used', MotionWhereUsedViewSet, basename='MotionWhereUsedText')
router.register(r'links', MotionLinkViewSet, basename='MotionLink')
router.register(r'', MotionViewSet, basename='Motion')

urlpatterns = [
    url(r'^(?P<motion_pk>\d+)/comments/$', MotionCommentViewSet.as_view({'get': 'retrieve', 'post': 'create'}), name="motion_comments"),
    url(r'^(?P<motion_pk>\d+)/votes/$', MotionVoteViewSet.as_view({'get': 'retrieve', 'post': 'create', 'put': 'update'}), name="motion_votes"),
]

urlpatterns += router.urls
