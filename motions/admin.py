# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from motions.models import Motion, MotionCategory, MotionDifficulty, DebateFormat, MotionAgeRange, MotionImproPrep, \
    MotionTrainingFocus, MotionType, MotionInfoText, MotionWhereUsed, MotionLink

admin.site.register(Motion)
admin.site.register(MotionCategory)
admin.site.register(MotionDifficulty)
admin.site.register(DebateFormat)
admin.site.register(MotionAgeRange)
admin.site.register(MotionType)
admin.site.register(MotionTrainingFocus)
admin.site.register(MotionImproPrep)
admin.site.register(MotionWhereUsed)
admin.site.register(MotionInfoText)
admin.site.register(MotionLink)
# admin.site.register(MotionComment)
# admin.site.register(MotionVote)
