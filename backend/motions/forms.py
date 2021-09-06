# forms.py

from django import forms
from django.contrib import admin
from motions.models import Motion
class MotionsForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(MotionsForm, self).__init__(*args, **kwargs)
        self.fields['tags'].widget = admin.widgets.AdminTextareaWidget()