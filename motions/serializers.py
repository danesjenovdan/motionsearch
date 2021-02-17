from rest_framework import serializers

from motions.models import MotionCategory, MotionDifficulty, DebateFormat, Motion, MotionAgeRange, MotionType, \
    MotionTrainingFocus, MotionImproPrep, MotionWhereUsed, MotionInfoText, MotionLink


class MotionCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MotionCategory
        fields = ['id', 'value']


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


# class MotionCommentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = MotionComment
#         fields = ['id', 'user', 'text']


# class CommenterSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Commenter
#         fields = ['id', 'user', 'text']


# class MotionVoteSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = MotionVote
#         fields = ['id', 'user', 'value']


# class VoterSerializer(serializers.ModelSerializer):
#     vote =
#     class Meta:
#         model = Voter
#         fields = ['id', 'motion', 'vote', 'created_at']


class MotionSerializer(serializers.ModelSerializer):
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
    # comments = MotionCommentSerializer(many=True)
    # votes = MotionVoteSerializer(many=True)

    class Meta:
        model = Motion
        fields = '__all__'
