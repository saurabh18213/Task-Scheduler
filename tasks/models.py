from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
import pytz
import datetime as Datetime
from django.core.validators import MinValueValidator
# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=255, default='Task')
    description = models.TextField(null=True)
    created_by = models.ForeignKey(User,related_name='tasks', on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(null=True)
    repeat = models.BooleanField(default=False)
    duration = models.DurationField(default=Datetime.timedelta(days=1, hours=0),
                validators=[MinValueValidator(Datetime.timedelta(days=0, hours=1, minutes=0))])
    completed_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name

    @property
    def is_past_due(self):
        now = datetime.now().astimezone(pytz.timezone("Asia/Kolkata"))
        dead = self.deadline.astimezone(pytz.timezone("Asia/Kolkata"))
        # print(dead.tzinfo,now.tzinfo)
        # print(dead.time(), now.time())

        if (dead.date() > now.date()):
            # print('case 1')
            return False
        elif ((dead.date() == now.date()) and (dead.time() >= now.time())):
            # print('case 2')
            return False
        else:
            # print('case 3')
            return True
             
class Notification(models.Model):
    time = models.DateTimeField(null=True) 
    task = models.ForeignKey(Task, related_name='notifications', on_delete=models.CASCADE, null=True)