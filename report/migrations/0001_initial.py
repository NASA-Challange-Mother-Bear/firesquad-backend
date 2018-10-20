# Generated by Django 2.1.2 on 2018-10-20 09:58

from django.conf import settings
import django.contrib.gis.db.models.fields
import django.contrib.postgres.fields
from django.contrib.postgres.operations import CreateExtension
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import report.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        CreateExtension('postgis'),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photos', django.contrib.postgres.fields.ArrayField(base_field=models.ImageField(upload_to=report.models.report_location), size=None)),
                ('geolocation', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('status', models.IntegerField(choices=[(0, 'Processing'), (1, 'Rejected'), (2, 'Accepted')])),
                ('type', models.IntegerField(choices=[(0, 'Forest Fire'), (1, 'Fire Hazard')])),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
