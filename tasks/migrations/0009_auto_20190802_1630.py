# Generated by Django 2.2.3 on 2019-08-02 11:00

import datetime
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0008_auto_20190801_2005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='duration',
            field=models.DurationField(default=datetime.timedelta(1), validators=[django.core.validators.MinValueValidator(datetime.timedelta(0, 3600))]),
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(default=datetime.datetime(2019, 8, 2, 16, 30, 54, 826400))),
                ('task', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='notifications', to='tasks.Task')),
            ],
        ),
    ]
