# Generated by Django 2.1.2 on 2018-10-20 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alert', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='alert',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]