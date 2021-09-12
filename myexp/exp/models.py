from django.db import models
from django.contrib.auth.models import User
from datetime import date
# Create your models here.

class Expense(models.Model):
    userid = models.ForeignKey(User,on_delete=models.DO_NOTHING)
    expense_date = models.DateField(default=date.today)
    expense_name = models.CharField(max_length=150)
    amount = models.IntegerField()