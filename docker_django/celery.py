from celery import Celery
from django.conf import settings
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'docker_django.settings')

app = Celery('docker_django')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()