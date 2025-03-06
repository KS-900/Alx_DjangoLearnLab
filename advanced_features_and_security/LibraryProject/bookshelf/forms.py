from django import forms
from django.contrib.auth.models import Group
from django.forms import ModelForm

class TeamForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['name']