# Generated by Django 2.1.2 on 2018-10-20 12:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0003_auto_20181020_1209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='alert',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='alerts', to='alert.Alert'),
        ),
    ]
