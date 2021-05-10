# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import viewsets, status, permissions, authentication
from rest_framework.response import Response
from rest_framework.decorators import action

from django_filters.rest_framework import DjangoFilterBackend, Filter, FilterSet
from django.shortcuts import get_object_or_404
from motions.models import MotionCategory, MotionDifficulty, DebateFormat, Motion, MotionAgeRange, MotionType, \
    MotionTrainingFocus, MotionImproPrep, MotionWhereUsed, MotionInfoText, MotionLink, MotionComment, MotionVote
from motions.serializers import MotionCategorySerializer, MotionDifficultySerializer, DebateFormatSerializer, \
    MotionAgeRangeSerializer, MotionTypeSerializer, MotionTrainingFocusSerializer, \
    MotionImproPrepSerializer, MotionWhereUsedSerializer, MotionInfoTextSerializer, MotionLinkSerializer, \
    MotionCommentSerializer, MotionDetailedSerializer, MotionSerializer, MotionVoteSerializer

from users.models import User

class MultiValueKeyFilter(Filter):
    def filter(self, qs, value):
        if not value:
            return qs
        
        self.lookup_expr = 'in'
        values = value.split(',')
        return super(MultiValueKeyFilter, self).filter(qs, values)

class MotionCategoryFilterSet(FilterSet):
    value = MultiValueKeyFilter(field_name='value')
    id = MultiValueKeyFilter(field_name='id')
    class Meta:
        model = MotionCategory
        fields = ('value','id')

class MotionFilterSet(FilterSet):
    id = MultiValueKeyFilter(field_name='id')
    age_range = MultiValueKeyFilter(field_name='age_range')
    debate_formats = MultiValueKeyFilter(field_name='debate_formats')
    type = MultiValueKeyFilter(field_name='type')
    impro_prep = MultiValueKeyFilter(field_name='impro_prep')
    training_focus = MultiValueKeyFilter(field_name='training_focus')
    category = MultiValueKeyFilter(field_name='category')
    difficulties = MultiValueKeyFilter(field_name='difficulties')

    class Meta:
        model = Motion
        fields = ('id', 'difficulties', 'age_range', 'impro_prep', 'debate_formats', 'type', 'training_focus', 'category')

class MotionCategoryViewSet(viewsets.ModelViewSet):
    queryset = MotionCategory.objects.all().order_by('value')
    serializer_class = MotionCategorySerializer
    filter_backends = (DjangoFilterBackend,)
    filter_class = MotionCategoryFilterSet
    filter_fields = ('value','id')
    permission_classes=[permissions.IsAuthenticatedOrReadOnly]


class MotionDifficultyViewSet(viewsets.ModelViewSet):
    queryset = MotionDifficulty.objects.all().order_by('value')
    serializer_class = MotionDifficultySerializer
    permission_classes=[permissions.IsAuthenticatedOrReadOnly,]



class DebateFormatViewSet(viewsets.ModelViewSet):
    queryset = DebateFormat.objects.all().order_by('value')
    serializer_class = DebateFormatSerializer
    permission_classes=[permissions.IsAuthenticatedOrReadOnly,]


class MotionAgeRangeViewSet(viewsets.ModelViewSet):
    queryset = MotionAgeRange.objects.all().order_by('value')
    serializer_class = MotionAgeRangeSerializer
    permission_classes=[permissions.IsAuthenticatedOrReadOnly,]


class MotionTypeViewSet(viewsets.ModelViewSet):
    queryset = MotionType.objects.all().order_by('value')
    serializer_class = MotionTypeSerializer
    permission_classes=[permissions.IsAuthenticatedOrReadOnly,]


class MotionTrainingFocusViewSet(viewsets.ModelViewSet):
    queryset = MotionTrainingFocus.objects.all().order_by('value')
    serializer_class = MotionTrainingFocusSerializer
    permission_classes=[permissions.IsAuthenticatedOrReadOnly,]


class MotionImproPrepViewSet(viewsets.ModelViewSet):
    queryset = MotionImproPrep.objects.all().order_by('value')
    serializer_class = MotionImproPrepSerializer
    permission_classes=[permissions.IsAuthenticatedOrReadOnly,]


class MotionWhereUsedViewSet(viewsets.ModelViewSet):
    queryset = MotionWhereUsed.objects.all().order_by('value')
    serializer_class = MotionWhereUsedSerializer
    permission_classes=[permissions.IsAuthenticatedOrReadOnly,]


class MotionInfoTextViewSet(viewsets.ModelViewSet):
    queryset = MotionInfoText.objects.all().order_by('value')
    serializer_class = MotionInfoTextSerializer
    permission_classes=[permissions.IsAuthenticatedOrReadOnly,]


class MotionLinkViewSet(viewsets.ModelViewSet):
    queryset = MotionLink.objects.all().order_by('value')
    serializer_class = MotionLinkSerializer
    permission_classes=[permissions.IsAuthenticatedOrReadOnly]

class MotionCommentViewSet(viewsets.ModelViewSet):
    queryset = MotionComment.objects.all().order_by('-created_at')
    serializer_class = MotionCommentSerializer
    lookup_field = 'motion_pk'
    permission_classes=[permissions.IsAuthenticatedOrReadOnly]

    def retrieve(self, request, *args, **kwargs):
        motion = Motion.objects.get(pk=kwargs.get('motion_pk', None))
        q = self.queryset.filter(motion=motion)
        return Response(data=self.serializer_class(q, many=True).data)
    def create(self, request, *args, **kwargs):
        motion = get_object_or_404(Motion, pk=kwargs.get('motion_pk', None))
        serializer = MotionCommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=False):
            serializer.save(user = request.user, motion = motion)
            return Response(serializer.data)
class MotionVoteViewSet(viewsets.ModelViewSet):
    queryset = MotionVote.objects.all().order_by('-created_at')
    serializer_class = MotionVoteSerializer
    lookup_field = 'motion_pk'
    permission_classes=[permissions.IsAuthenticatedOrReadOnly]

    def retrieve(self, request, *args, **kwargs):
        motion = Motion.objects.get(pk=kwargs.get('motion_pk', None))
        q = self.queryset.filter(motion=motion)
        return Response(data=self.serializer_class(q, many=True).data)
    def create(self, request, *args, **kwargs):
        motion = get_object_or_404(Motion, pk=kwargs.get('motion_pk', None))
        motionVote = get_object_or_404(MotionVote, motion = motion, user = request.user)
        if(not motionVote):
            motionVote = {}
        CHOICES = (
            (1, 1),
            (2, -1),
            (3, 0)
        )
        vote = dict(CHOICES)[request.data.get('choices', 3)]
        previous_vote = dict(CHOICES)[motionVote.choices]
        if (motionVote.user == request.user):
            motion.votes += -previous_vote + vote
            motion.save()
            motionVote.choices = request.data.get('choices', 3)
            motionVote.save()
            return Response({"user":request.user.username, "motionScore": motion.votes, "vote": request.data.get('choices', 3) })
        else: 
            serializer = MotionVoteSerializer(data=request.data)
            if serializer.is_valid(raise_exception=False):
                serializer.save(user = request.user, motion = motion)
                motion.votes += vote
                return Response(serializer.data)

class MotionViewSet(viewsets.ModelViewSet):
    queryset = Motion.objects.all()
    serializer_class = MotionSerializer  # for basic info - topic and category
    serializer_detailed_class = MotionDetailedSerializer  # for detailed info - all Motion model fields
    filter_backends = (DjangoFilterBackend,)
    filter_class = MotionFilterSet
    filter_fields = ('id', 'difficulties', 'age_range', 'impro_prep', 'debate_formats', 'type', 'training_focus', 'category')

    def get_serializer_class(self):
        if self.request.query_params.get('detailed', False):  # arg for detailed motion info
            return self.serializer_detailed_class
        return super(MotionViewSet, self).get_serializer_class()

    def create(self, request, *args, **kwargs):
        categories_data = request.data.get('categories', [])
        where_used_data = request.data.get('where_used', [])
        info_text_data = request.data.get('info_text', [])
        links_data = request.data.get('links', [])

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save()
        instance = serializer.instance
        for where_used in where_used_data: 
            response, created = MotionWhereUsed.objects.get_or_create(
                **where_used
            )
            instance.where_used.add(response)
        for info_text in info_text_data: 
            response, created = MotionInfoText.objects.get_or_create(
                **info_text
            )
            instance.info_text.add(response)
        for links in links_data: 
            response, created = MotionLink.objects.get_or_create(
                **links
            )
            instance.links.add(response)
        for category_data in categories_data: 
            category, created = MotionCategory.objects.get_or_create(
                **category_data
            )
            instance.category.add(category)

        headers = self.get_success_headers(serializer.data)

        data = self.get_serializer(instance).data
        return Response(data, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        categories_data = request.data.get('category', [])
        where_used_data = request.data.get('where_used', [])
        info_text_data = request.data.get('info_text', [])
        links_data = request.data.get('links', [])

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save()
        instance = serializer.instance
        for where_used in where_used_data: 
            response, created = MotionWhereUsed.objects.get_or_create(
                **where_used
            )
            instance.where_used.add(response)
        for info_text in info_text_data: 
            response, created = MotionInfoText.objects.get_or_create(
                **info_text
            )
            instance.info_text.add(response)
        for links in links_data: 
            response, created = MotionLink.objects.get_or_create(
                **links
            )
            instance.links.add(response)
        for category_data in categories_data: 
            category, created = MotionCategory.objects.get_or_create(
                **category_data
            )
            instance.category.add(category)

        headers = self.get_success_headers(serializer.data)

        data = self.get_serializer(instance).data
        return Response(data, status=status.HTTP_200_OK, headers=headers)