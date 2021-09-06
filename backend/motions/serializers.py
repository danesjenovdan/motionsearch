from rest_framework import serializers

from motions.models import MotionCategory, MotionDifficulty, DebateFormat, Motion, MotionAgeRange, MotionType, \
    MotionTrainingFocus, MotionImproPrep, MotionWhereUsed, MotionInfoText, MotionLink, MotionComment, MotionVote

from django.db import models
from django.utils import timezone
from django.shortcuts import get_object_or_404


class AutoDateTimeField(models.DateTimeField):
    def pre_save(self, model_instance, add):
        return timezone.now()

class MotionCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MotionCategory
        fields = ['id', 'value']
        required_fields = ['id']
    #def create(self, validated_data):
    #    category = MotionCategory.objects.get_or_create(**validated_data)
    #    return category
class MotionKeywordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MotionCategory
        fields = ['id', 'value']
        required_fields = ['id']
    #def create(self, validated_data):
    #    category = MotionCategory.objects.get_or_create(**validated_data)
    #    return category
class MotionDifficultySerializer(serializers.ModelSerializer):
    class Meta:
        model = MotionDifficulty
        fields = ['id', 'value']
        required_fields = ['id']


class DebateFormatSerializer(serializers.ModelSerializer):
    class Meta:
        model = DebateFormat
        fields = ['id', 'value']


class MotionAgeRangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = MotionAgeRange
        fields = ['id', 'value']


class MotionTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = MotionType
        fields = ['id', 'value']


class MotionTrainingFocusSerializer(serializers.ModelSerializer):
    class Meta:
        model = MotionTrainingFocus
        fields = ['id', 'value']


class MotionImproPrepSerializer(serializers.ModelSerializer):
    class Meta:
        model = MotionImproPrep
        fields = ['id', 'value']


class MotionWhereUsedSerializer(serializers.ModelSerializer):
    class Meta:
        model = MotionWhereUsed
        fields = ['id', 'value']


class MotionInfoTextSerializer(serializers.ModelSerializer):
    class Meta:
        model = MotionInfoText
        fields = ['id', 'value']
        required_fields = ['id']

class MotionLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = MotionLink
        fields = ['id', 'value', 'text']


class MotionCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = MotionComment
        fields = ['id', 'user', 'text', 'created_at']
class MotionVoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = MotionVote
        fields = ['id', 'user', 'choices', 'motion']


class MotionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Motion
        #fields = ['id', 'topic', 'category', 'created_at', 'debate_formats', 'age_range', 
        #'type', 'training_focus', 'impro_prep', 'where_used', 'info_text', 'links']
        fields = ['id', 'topic', 'category', 'keywords', 'created_at', 'difficulties', 'age_range', 
        'impro_prep', 'debate_formats', 'type', 'training_focus',  'where_used', 'info_text', 'links', 'votes', 'user']
        read_only_fields = ['category', "info_text", "where_used", "links", "keywords"]


class MotionDetailedSerializer(serializers.ModelSerializer):
    category = MotionCategorySerializer(many=True)
    keywords = MotionKeywordsSerializer(many=True)
    difficulties = MotionDifficultySerializer(many=True)
    debate_formats = DebateFormatSerializer(many=True)
    age_range = MotionAgeRangeSerializer(many=True)
    type = MotionTypeSerializer(many=True)
    training_focus = MotionTrainingFocusSerializer(many=True)
    impro_prep = MotionImproPrepSerializer(many=True)
    where_used = MotionWhereUsedSerializer(many=True)
    info_text = MotionInfoTextSerializer(many=True)
    links = MotionLinkSerializer(many=True),

    class Meta:
        model = Motion
        fields = '__all__'
