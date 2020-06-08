from django import forms
from .models import Profile, Project

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']