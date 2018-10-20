# Generated by Django 2.1.2 on 2018-10-20 11:19

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alert',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('geolocation', django.contrib.gis.db.models.fields.PointField(srid=4326)),
            ],
        ),
    ]