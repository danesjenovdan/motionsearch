# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import viewsets
from rest_framework.response import Response

from motions.models import MotionCategory, MotionDifficulty, DebateFormat, Motion, MotionAgeRange, MotionType, \
    MotionTrainingFocus, MotionImproPrep, MotionWhereUsed, MotionInfoText, MotionLink, MotionComment
from motions.serializers import MotionCategorySerializer, MotionDifficultySerializer, DebateFormatSerializer, \
    MotionAgeRangeSerializer, MotionTypeSerializer, MotionTrainingFocusSerializer, \
    MotionImproPrepSerializer, MotionWhereUsedSerializer, MotionInfoTextSerializer, MotionLinkSerializer, \
    MotionCommentSerializer, MotionDetailedSerializer, MotionSerializer


class MotionCategoryViewSet(viewsets.ModelViewSet):
    queryset = MotionCategory.objects.all().order_by('value')
    serializer_class = MotionCategorySerializer


class MotionDifficultyViewSet(viewsets.ModelViewSet):
    queryset = MotionDifficulty.objects.all().order_by('value')
    serializer_class = MotionDifficultySerializer


class DebateFormatViewSet(viewsets.ModelViewSet):
    queryset = DebateFormat.objects.all().order_by('value')
    serializer_class = DebateFormatSerializer


class MotionAgeRangeViewSet(viewsets.ModelViewSet):
    queryset = MotionAgeRange.objects.all().order_by('value')
    serializer_class = MotionAgeRangeSerializer


class MotionTypeViewSet(viewsets.ModelViewSet):
    queryset = MotionType.objects.all().order_by('value')
    serializer_class = MotionTypeSerializer


class MotionTrainingFocusViewSet(viewsets.ModelViewSet):
    queryset = MotionTrainingFocus.objects.all().order_by('value')
    serializer_class = MotionTrainingFocusSerializer


class MotionImproPrepViewSet(viewsets.ModelViewSet):
    queryset = MotionImproPrep.objects.all().order_by('value')
    serializer_class = MotionImproPrepSerializer


class MotionWhereUsedViewSet(viewsets.ModelViewSet):
    queryset = MotionWhereUsed.objects.all().order_by('value')
    serializer_class = MotionWhereUsedSerializer


class MotionInfoTextViewSet(viewsets.ModelViewSet):
    queryset = MotionInfoText.objects.all().order_by('value')
    serializer_class = MotionInfoTextSerializer


class MotionLinkViewSet(viewsets.ModelViewSet):
    queryset = MotionLink.objects.all().order_by('value')
    serializer_class = MotionLinkSerializer


class MotionCommentViewSet(viewsets.ModelViewSet):
    queryset = MotionComment.objects.all().order_by('-created_at')
    serializer_class = MotionCommentSerializer
    lookup_field = 'motion_pk'

    def retrieve(self, request, *args, **kwargs):
        motion = Motion.objects.get(pk=kwargs.get('motion_pk', None))
        q = self.queryset.filter(motion=motion)
        return Response(data=self.serializer_class(q, many=True).data)


class MotionViewSet(viewsets.ModelViewSet):
    queryset = Motion.objects.all()
    serializer_class = MotionSerializer  # for basic info - topic and category
    serializer_detailed_class = MotionDetailedSerializer  # for detailed info - all Motion model fields

    def get_serializer_class(self):
        if self.request.query_params.get('detailed', False):  # arg for detailed motion info
            return self.serializer_detailed_class
        return super(MotionViewSet, self).get_serializer_class()
