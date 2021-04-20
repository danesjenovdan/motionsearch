from rest_framework import serializers

from motions.models import MotionCategory, MotionDifficulty, DebateFormat, Motion, MotionAgeRange, MotionType, \
    MotionTrainingFocus, MotionImproPrep, MotionWhereUsed, MotionInfoText, MotionLink, MotionComment

from django.db import models
from django.utils import timezone


class AutoDateTimeField(models.DateTimeField):
    def pre_save(self, model_instance, add):
        return timezone.now()

class MotionCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MotionCategory
        fields = ['id', 'value']
        def create(self, validated_data):
            category = MotionCategory.objects.get_or_create(**validated_data)
            return category

class MotionDifficultySerializer(serializers.ModelSerializer):
    class Meta:
        model = MotionDifficulty
        fields = ['id', 'value']


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


class MotionLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = MotionLink
        fields = ['id', 'value']


class MotionCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = MotionComment
        fields = ['id', 'user', 'text']


class MotionSerializer(serializers.ModelSerializer):
    category = MotionCategorySerializer(many=True)

    class Meta:
        model = Motion
        fields = ['id', 'topic', 'category', 'created_at']
    
    def create(self, validated_data):
        categories_data = validated_data.pop('category')
        motion = Motion.objects.create(**validated_data)
        topics = []
        for category_data in categories_data:
            category = MotionCategory.objects.create(motion=motion, **category_data)
            motion.category.add(category)
        return motion

    def update(motion, self, validated_data):
        categories_data = validated_data.pop('category')
        motion = Motion.objects.create(**validated_data)
        topics = []
        for category_data in categories_data:
            category = MotionCategory.objects.create(motion=motion, **category_data)
            motion.category.add(category)
        return motion


class MotionDetailedSerializer(serializers.ModelSerializer):
    category = MotionCategorySerializer(many=True)
    difficulties = MotionDifficultySerializer(many=True)
    debate_formats = DebateFormatSerializer(many=True)
    age_range = MotionAgeRangeSerializer(many=True)
    type = MotionTypeSerializer(many=True)
    training_focus = MotionTrainingFocusSerializer(many=True)
    impro_prep = MotionImproPrepSerializer(many=True)
    where_used = MotionWhereUsedSerializer(many=True)
    info_text = MotionInfoTextSerializer(many=True)
    links = MotionLinkSerializer(many=True)

    class Meta:
        model = Motion
        fields = '__all__'
