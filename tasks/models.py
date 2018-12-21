from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
import pytz
# Create your models here.
class Task(models.Model):
    description = models.CharField(max_length=255)
    created_by = models.ForeignKey(User,related_name='tasks', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField()
    completed_at = models.DateTimeField(null=True, blank=True)

    @property
    def is_past_due(self):
        now = datetime.now()
        dead = self.deadline.astimezone(pytz.timezone("Asia/Kolkata"))
        print(dead.tzinfo,now.tzinfo)
        print(dead.time(), now.time())

        if (dead.date() > now.date()):
            print('case 1')
            return False
        elif ((dead.date() == now.date()) and (dead.time() >= now.time())):
            print('case 2')
            return False
        else:
            print('case 3')
            return True
             
    