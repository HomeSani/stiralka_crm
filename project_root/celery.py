import os

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project_root.settings')

app = Celery('project_root')

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'create_cells_for_two_weeks_task': {
        'task': 'schedule.tasks.create_cells_for_two_weeks_task',
        'schedule': crontab(minute='0', hour='0', day_of_month='*/14'),
        'args': (),
    },
    'set_for_all_users_restricton_on_use_task': {
        'task': 'schedule.tasks.set_for_all_users_restricton_on_use_task',
        'schedule': crontab(minute='0', hour='0', day_of_week='1'),
        'args': (),
    },
}
