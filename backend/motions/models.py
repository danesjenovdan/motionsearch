# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import uuid
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
    def __str__(self):
        return self.value
class MotionKeywords(BaseModel):
    value = models.CharField(max_length=255, null=True, blank=True)
    def __str__(self):
        return self.value

class MotionDifficulty(BaseModel):
    value = models.CharField(max_length=255, null=True, blank=True)
    def __str__(self):
        return self.value


class DebateFormat(BaseModel):
    value = models.CharField(max_length=255, null=False, blank=False)
    def __str__(self):
        return self.value


class MotionAgeRange(BaseModel):
    value = models.CharField(max_length=255, null=False, blank=False)
    def __str__(self):
        return self.value


class MotionType(BaseModel):
    value = models.CharField(max_length=255, null=False, blank=False)
    def __str__(self):
        return self.value


class MotionTrainingFocus(BaseModel):
    value = models.CharField(max_length=255, null=False, blank=False)
    def __str__(self):
        return self.value


class MotionImproPrep(BaseModel):
    value = models.CharField(max_length=255, null=False, blank=False)
    def __str__(self):
        return self.value


class MotionWhereUsed(BaseModel):
    value = models.CharField(max_length=255, null=False, blank=False)
    def __str__(self):
        return self.value


class MotionInfoText(BaseModel):
    value = models.TextField( null=True, blank=True)
    def __str__(self):
        return str(self.value)

class MotionLink(BaseModel):
    text = models.TextField( null=True, blank=True)
    value = models.URLField(null=True, blank=True)
    def __str__(self):
        return str(self.value)


class MotionComment(BaseModel):
    user = models.ForeignKey('users.User', null=True, blank=False, on_delete=models.SET_NULL)
    text = models.TextField(null=False, blank=False)
    motion = models.ForeignKey('motions.Motion', null=False, blank=False,on_delete=models.CASCADE)
    created_at = AutoDateTimeField(auto_now=True)

class MotionVote(BaseModel):
    user = models.ForeignKey('users.User', null=True, blank=False, on_delete=models.CASCADE)
    choices = models.PositiveSmallIntegerField(
       choices=VoteValue.CHOICES,
       default=3,
   )
    motion = models.ForeignKey('motions.Motion', null=False, blank=False,on_delete=models.CASCADE)
    
    class Meta:
        unique_together = ('user', 'motion',)

class Motion(BaseModel):
    topic = models.TextField(blank=True, null=True)
    category = models.ManyToManyField(MotionCategory, blank=True, related_name="motions")
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
    user = models.ForeignKey('users.User', null=True, blank=False, on_delete=models.CASCADE)
    keywords =  models.ManyToManyField(MotionKeywords, blank=True, related_name="motions")

    @property
    def quality_score(self):
        return 0

    @property
    def leaning_score(self):
        return 0

    def __str__(self):
        return str(self.topic)

