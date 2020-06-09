from django import forms
from .models import Profile, Project, review

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['profile', 'pub_date']

class ReviewForm(forms.ModelForm):
    class Meta:
        model = review
        exclude = ['user', 'project']