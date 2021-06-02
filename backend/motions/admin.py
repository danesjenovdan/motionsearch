# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from motions.models import Motion, MotionCategory, MotionDifficulty, DebateFormat, MotionAgeRange, MotionImproPrep, \
    MotionTrainingFocus, MotionType, MotionInfoText, MotionWhereUsed, MotionLink, MotionComment


class MotionsAdmin(admin.ModelAdmin):
    model = Motion
    list_display = [
        'id',
        'topic',
        'user',
        'created_at'
    ]
admin.site.register(Motion, MotionsAdmin)
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
admin.site.register(MotionComment)
