# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.translation import gettext as _
from django.db import models
from motions.behaviors.models import BaseModel
from django.db import models
from django.utils import timezone


class AutoDateTimeField(models.DateTimeField):
    def pre_save(self, model_instance, add):
        return timezone.now()




class VoteValue:
    UPVOTE = 1
    DOWNVOTE = -1

    CHOICES = (
        (1, _('Upvote')),
        (2, _('Downvote')),
        (3, _('No vote'))
    )


class MotionCategory(BaseModel):
    value = models.CharField(max_length=255, null=True, blank=True)


class MotionDifficulty(BaseModel):
    value = models.CharField(max_length=255, null=True, blank=True)


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
    value = models.TextField( null=True, blank=True)


class MotionLink(BaseModel):
    value = models.URLField(null=True, blank=True)


class MotionComment(BaseModel):
    user = models.ForeignKey('users.User', null=True, blank=False, on_delete=models.SET_NULL)
    text = models.TextField(null=False, blank=False)
    motion = models.ForeignKey('motions.Motion', null=False, blank=False,on_delete=models.CASCADE)

class MotionVote(BaseModel):
    user = models.ForeignKey('users.User', null=True, blank=False, on_delete=models.CASCADE,  unique=True)
    choices = models.PositiveSmallIntegerField(
       choices=VoteValue.CHOICES,
       default=3,
   )
    motion = models.ForeignKey('motions.Motion', null=False, blank=False,on_delete=models.CASCADE)

class Motion(BaseModel):
    topic = models.TextField(blank=True, null=True)
    category = models.ManyToManyField(MotionCategory, blank=True)
    difficulties = models.ForeignKey(MotionDifficulty, on_delete=models.CASCADE)
    debate_formats = models.ForeignKey(DebateFormat, on_delete=models.CASCADE)
    age_range = models.ForeignKey(MotionAgeRange, on_delete=models.CASCADE)
    type = models.ForeignKey(MotionType, on_delete=models.CASCADE)
    training_focus = models.ForeignKey(MotionTrainingFocus, on_delete=models.CASCADE)
    impro_prep = models.ForeignKey(MotionImproPrep, on_delete=models.CASCADE)
    where_used = models.ManyToManyField(MotionWhereUsed, blank=True)
    info_text = models.ManyToManyField(MotionInfoText, blank=True)
    links = models.ManyToManyField(MotionLink, blank=True)
    votes = models.IntegerField(default=0, blank=True, db_index=True)

    @property
    def quality_score(self):
        return 0

    @property
    def leaning_score(self):
        return 0
