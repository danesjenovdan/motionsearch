# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import viewsets, mixins, permissions

from motions.models import MotionCategory, MotionDifficulty, DebateFormat, Motion, MotionAgeRange
from motions.serializers import MotionCategorySerializer, MotionDifficultySerializer, DebateFormatSerializer, \
    MotionSerializer, MotionAgeRangeSerializer


class MotionCategoryViewSet(viewsets.ModelViewSet):
    queryset = MotionCategory.objects.all()
    serializer_class = MotionCategorySerializer


class MotionDifficultyViewSet(viewsets.ModelViewSet):
    queryset = MotionDifficulty.objects.all()
    serializer_class = MotionDifficultySerializer


class DebateFormatViewSet(viewsets.ModelViewSet):
    queryset = DebateFormat.objects.all()
    serializer_class = DebateFormatSerializer


class MotionAgeRangeViewSet(viewsets.ModelViewSet):
    queryset = MotionAgeRange.objects.all()
    serializer_class = MotionAgeRangeSerializer


class MotionViewSet(viewsets.ModelViewSet):
    queryset = Motion.objects.all()
    serializer_class = MotionSerializer
