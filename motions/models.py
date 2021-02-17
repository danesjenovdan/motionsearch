# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.translation import gettext as _
from django.db import models
from motions.behaviors.models import BaseModel


class VoteValue(object):
    UPVOTE = 1
    DOWNVOTE = -1

    CHOICES = (
        (UPVOTE, _('Upvote')),
        (DOWNVOTE, _('Downvote')),
    )


class MotionCategory(BaseModel):
    value = models.CharField(max_length=255, null=False, blank=False)


class MotionDifficulty(BaseModel):
    value = models.CharField(max_length=255, null=False, blank=False)


class DebateFormat(BaseModel):
    value = models.CharField(max_length=255, null=False, blank=False)


class MotionAgeRange(BaseModel):
    value = models.CharField(max_length=255, null=False, blank=False)


class MotionType(BaseModel):
    value = models.CharField(max_length=255, null=False, blank=False)


class MotionTrainingFocus(BaseModel):
    value = models.CharField(max_length=255, null=False, blank=False)


class MotionImproPrep(BaseModel):
    value = models.CharField(max_length=255, null=False, blank=False)


class MotionWhereUsed(BaseModel):
    value = models.CharField(max_length=255, null=False, blank=False)


class MotionInfoText(BaseModel):
    value = models.TextField(null=False, blank=False)


class MotionLink(BaseModel):
    value = models.URLField(null=True, blank=True)


class MotionComment(BaseModel):
    user = models.ForeignKey('users.User', null=True, on_delete=models.SET_NULL)
    text = models.TextField(null=False, blank=False)


# class MotionVote(BaseModel):
#     user = models.ForeignKey('users.User', null=True, on_delete=models.SET_NULL)
#     value = models.IntegerField(choices=VoteValue.CHOICES)


class Motion(BaseModel):
    topic = models.TextField(blank=True, null=True)
    category = models.ManyToManyField(MotionCategory, blank=True, related_name='motion_category')
    difficulties = models.ManyToManyField(MotionDifficulty, blank=True, related_name='motion_difficulty')
    debate_formats = models.ManyToManyField(DebateFormat, blank=True, related_name='debate_format')
    age_range = models.ManyToManyField(MotionAgeRange, blank=True, related_name='age_range')
    type = models.ManyToManyField(MotionType, blank=True, related_name='type')
    training_focus = models.ManyToManyField(MotionTrainingFocus, blank=True, related_name='training_focus')
    impro_prep = models.ManyToManyField(MotionImproPrep, blank=True, related_name='impro_prep')
    where_used = models.ManyToManyField(MotionWhereUsed, blank=True, related_name='where_used')
    info_text = models.ManyToManyField(MotionInfoText, blank=True, related_name='info_text')
    links = models.ManyToManyField(MotionLink, blank=True, related_name='links')
    comments = models.ManyToManyField(MotionComment, blank=True, related_name='comments')
    # votes = models.ManyToManyField(MotionVote, blank=True, related_name='votes')

    @property
    def quality_score(self):
        return 0

    @property
    def leaning_score(self):
        return 0


# class Voter(models.Model):
#     motion = models.ForeignKey(Motion, on_delete=models.CASCADE)
#     vote = models.ForeignKey(MotionVote, on_delete=models.SET_NULL)
#     created_at = models.DateField(auto_now_add=True)
#
#
# class Commenter(models.Model):
#     motion = models.ForeignKey(Motion, on_delete=models.CASCADE)
#     comment = models.ForeignKey(MotionComment, on_delete=models.SET_NULL)
#     created_at = models.DateField(auto_now_add=True)

