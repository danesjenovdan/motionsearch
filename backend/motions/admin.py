# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from django import forms
from django.utils.translation import ugettext_lazy as _
from import_export import resources
from import_export.admin import  ImportExportModelAdmin
from django.contrib.admin.widgets import FilteredSelectMultiple

from motions.models import Motion, MotionCategory, MotionDifficulty, DebateFormat, MotionAgeRange, MotionImproPrep, \
    MotionTrainingFocus, MotionType, MotionInfoText, MotionWhereUsed, MotionLink, MotionComment, MotionKeywords
from users.models import User

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
            category.motions.set(self.cleaned_data['motions'])
            self.save_m2m()

        return category

class CategoryAdmin(admin.ModelAdmin):
    form = CategoryAdminForm

def valueToId(Model, row, rowName):
    values = row[rowName].split(',')
    if len(values) == 1 and values[0] == '':
        return ''
    ids = []
    for value in values:
        res = Model.objects.filter(value=value).first()
        ids += [res.id]
    return ','.join(str(x) for x in ids)

def usernameToId(username):
    user = User.objects.filter(username=username).first()
    return user.id

def textsToId(Model, row, rowName):
    values = row[rowName].split(',')
    if len(values) == 1 and values[0] == '':
        return ''
    ids = []
    for value in values:
        res = Model.objects.get_or_create(
                value=value
            )
        ids += [res[0].id]
    return ','.join(str(x) for x in ids)
class MotionResource(resources.ModelResource):
    def before_import_row(self, row, **kwargs):
        category = valueToId(MotionCategory, row, 'category')
        difficulties = valueToId(MotionDifficulty, row, 'difficulties')
        debate_formats = valueToId(DebateFormat, row, 'debate_formats')
        age_range = valueToId(MotionAgeRange, row, 'age_range')
        type = valueToId(MotionType, row, 'type')
        training_focus = valueToId(MotionTrainingFocus, row, 'training_focus')
        impro_prep = valueToId(MotionImproPrep, row, 'impro_prep')
        user = usernameToId(row['user'])
        info_text = textsToId(MotionInfoText, row, 'info_text')
        where_used = textsToId(MotionWhereUsed, row, 'where_used')
        links = textsToId(MotionLink, row, 'links')
        keywords = textsToId(MotionKeywords, row, 'keywords')

        row['category'] = category
        row['difficulties'] = difficulties
        row['debate_formats'] = debate_formats
        row['age_range'] = age_range
        row['type'] = type
        row['training_focus'] = training_focus
        row['impro_prep'] = impro_prep
        row['info_text'] = info_text
        row['where_used'] = where_used
        row['links'] = links
        row['user'] = user
        row['keywords'] = keywords

        return super().before_import_row(row, **kwargs)

    class Meta:
        model = Motion
class MotionsAdmin(ImportExportModelAdmin):
    resource_class = MotionResource
    model = Motion
    filter_horizontal = ('category', 'keywords') #If you don't specify this, you will get a multiple select widget.
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
admin.site.register(MotionKeywords)

