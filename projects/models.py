from django.db import models

# Create your models here.
class Profile(models.Model):
    profile_pic = models.ImageField(upload_to='image/', default="image/male.png", blank=True)
    bio = models.TextField(blank=True)
    contact_info = models.CharField(max_length=60)