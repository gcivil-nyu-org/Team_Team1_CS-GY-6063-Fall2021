from __future__ import absolute_import, unicode_literals

import os

from celery import Celery

from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "VMentalHealth.settings")

celery_app = Celery("VMentalHealth")
celery_app.config_from_object(settings, namespace="CELERY")
celery_app.conf.beat_schedule = {
    "appointments_update_task": {
        "task": "booking.tasks.appointments_update",
        "schedule": 5,
    },
}

celery_app.autodiscover_tasks()

@celery_app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))