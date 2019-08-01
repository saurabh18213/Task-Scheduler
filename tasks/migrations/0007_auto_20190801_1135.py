# Generated by Django 2.2.3 on 2019-08-01 06:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0006_auto_20190731_2258'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='repeat_duration',
        ),
        migrations.AddField(
            model_name='task',
            name='duration',
            field=models.DurationField(default=datetime.timedelta(1)),
        ),
    ]