# Generated by Django 2.2.3 on 2019-08-02 12:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0015_auto_20190802_1818'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='task',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='notifications', to='tasks.Task'),
        ),
    ]
