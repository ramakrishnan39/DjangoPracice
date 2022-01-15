from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
  name = models.CharField(blank=True, null=True, max_length=300)
  username = models.CharField(blank=True, null=True, max_length=30)
  email = models.EmailField(blank=True, null=True)
  bio = models.CharField(blank=True, null=True, max_length=300)
  pic = models.ImageField(blank=True, null=True, default='images/default.jpg', upload_to = 'propic/')


  def __str__(self) -> str:
      return self.username
