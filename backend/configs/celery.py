import os
from celery.schedules import crontab
from celery import Celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'configs.settings')

app = Celery('settings')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'send_spam_every_minutes':{
        'task': 'core.services.email_service.spam',
        'schedule': crontab()
        # 'args': (),
    }
}
