from .models import Task, Notification
from datetime import datetime
import datetime as Datetime
from django.db.models import Min
import pytz
from django.template.loader import render_to_string
from django.core.mail import EmailMessage

def notify():
    nots = Notification.objects.filter(time__lte=datetime.now().astimezone(pytz.timezone("Asia/Kolkata")))
    current_time = datetime.now().astimezone(pytz.timezone("Asia/Kolkata"))

    for notification in nots:
        task = notification.task
        Notification.objects.filter(task=task).delete()

        if(task.repeat):
            new_notification = Notification(time=current_time + task.duration,
            task=task);
            new_notification.save();

        mail_subject = "Please complete" + task.name
        message = render_to_string('notification.html', {
            'task': task
        })
        to_email = task.created_by.email
        email = EmailMessage(
                    mail_subject, message, to=[to_email]
        )
        email.send()    
    
    return