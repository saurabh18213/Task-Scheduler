from celery.task.schedules import crontab
from celery.decorators import periodic_task
from .notification_mail import notify



@periodic_task(
    run_every=(crontab(minute='*/10')),
    name="notify",
    ignore_result=True
)
def send_notofications():
    notify()