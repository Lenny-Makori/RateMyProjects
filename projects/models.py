from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='image/', default="image/male.png", blank=True)
    bio = models.TextField(blank=True)
    contact_info = models.CharField(max_length=60)


class Project(models.Model):
    project_image = models.ImageField(upload_to='image/')
    project_title = models.CharField(max_length=60)
    project_description = models.TextField()
    project_link = models.CharField(max_length=150)
    profile = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)