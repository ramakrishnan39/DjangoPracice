# Generated by Django 2.2 on 2021-09-17 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exp', '0003_expense_expense_desc'),
    ]

    operations = [
        migrations.AddField(
            model_name='expense',
            name='expense_month',
            field=models.CharField(default='September', max_length=12),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='expense',
            name='expense_year',
            field=models.CharField(default=2021, max_length=4),
            preserve_default=False,
        ),
    ]