from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='image/', default="image/male.png", blank=True)
    bio = models.TextField(blank=True)
    contact_info = models.CharField(max_length=60)

    @classmethod
    def get_profile(cls, user_id):
        profile = cls.objects.get(user=user_id)
        return profile

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Project(models.Model):
    project_image = models.ImageField(upload_to='image/')
    project_title = models.CharField(max_length=60)
    project_description = models.TextField()
    project_link = models.CharField(max_length=150)
    profile = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)


class review(models.Model):
    review = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)