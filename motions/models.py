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
    category = models.ManyToManyField(MotionCategory, blank=True)
    difficulties = models.ManyToManyField(MotionDifficulty, blank=True)
    debate_formats = models.ManyToManyField(DebateFormat, blank=True)
    age_range = models.ManyToManyField(MotionAgeRange, blank=True)
    type = models.ManyToManyField(MotionType, blank=True)
    training_focus = models.ManyToManyField(MotionTrainingFocus, blank=True)
    impro_prep = models.ManyToManyField(MotionImproPrep, blank=True)
    where_used = models.ManyToManyField(MotionWhereUsed, blank=True)
    info_text = models.ManyToManyField(MotionInfoText, blank=True)
    links = models.ManyToManyField(MotionLink, blank=True)
    comments = models.ManyToManyField(MotionComment, blank=True)
    # votes = models.ManyToManyField(MotionVote, blank=True)

    @property
    def quality_score(self):
        return 0

    @property
    def leaning_score(self):
        return 0
