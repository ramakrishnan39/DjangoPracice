from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

# Create your models here.
class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
  name = models.CharField(blank=True, null=True, max_length=300)
  username = models.CharField(blank=True, null=True, max_length=30)
  email = models.EmailField(blank=True, null=True)
  bio = models.CharField(blank=True, null=True, max_length=300)
  pic = models.ImageField(blank=True, null=True, default='default.jpg', upload_to = 'propic/')


  def __str__(self) -> str:
      return self.username

@receiver(post_save, sender=User)
def createProfile(sender, instance, created, **kwargs):
  if created:
    Profile.objects.create(user=instance, name=instance.first_name, email=instance.email, username=instance.username)
