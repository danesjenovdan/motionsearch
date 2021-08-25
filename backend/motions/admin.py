# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from django import forms
from django.utils.translation import ugettext_lazy as _
from import_export import resources
from import_export.admin import  ImportExportModelAdmin
from django.contrib.admin.widgets import FilteredSelectMultiple

from motions.models import Motion, MotionCategory, MotionDifficulty, DebateFormat, MotionAgeRange, MotionImproPrep, \
    MotionTrainingFocus, MotionType, MotionInfoText, MotionWhereUsed, MotionLink, MotionComment

class CategoryAdminForm(forms.ModelForm):
    motions = forms.ModelMultipleChoiceField(
        queryset=Motion.objects.all(),
        required=False,
        widget=FilteredSelectMultiple(
        verbose_name=_('Motions'),
        is_stacked=False
        )
    )
    class Meta:
        model = MotionCategory
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(CategoryAdminForm, self).__init__(*args, **kwargs)

        if self.instance and self.instance.pk:
            self.fields['motions'].initial = self.instance.motions.all()

    def save(self, commit=True):
        category = super(CategoryAdminForm, self).save(commit=False)

        if commit:
            category.save()

        if category.pk:
            print("yeeet 1")
            category.motions.set(self.cleaned_data['motions'])
            print("yeeet 2")
            self.save_m2m()

        return category

class CategoryAdmin(admin.ModelAdmin):
    form = CategoryAdminForm
class MotionResource(resources.ModelResource):
    class Meta:
        model = Motion
class MotionsAdmin(ImportExportModelAdmin):
    resource_class = MotionResource
    model = Motion
    filter_horizontal = ('category',) #If you don't specify this, you will get a multiple select widget.
    list_display = [
        'id',
        'topic',
        'user',
        'created_at'
    ]
    list_display_links = ('topic', 'id')



admin.site.register(Motion, MotionsAdmin)
admin.site.register(MotionCategory, CategoryAdmin)
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
