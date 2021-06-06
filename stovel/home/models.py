from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Book(models.Model):
    book_name = models.CharField(max_length=150)
    author_name = models.TextField()
    publication_name = models.TextField()
    posted_by = models.ForeignKey(User,on_delete=models.DO_NOTHING)

class Friends(models.Model):
    usr = models.CharField(max_length=200)
    frnd = models.ForeignKey(User,on_delete=models.DO_NOTHING)