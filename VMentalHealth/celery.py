from __future__ import absolute_import, unicode_literals

import os

from celery import Celery

from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "VMentalHealth.settings")

celery_app = Celery(
    "VMentalHealth",
    broker="amqps://wektanqn:Q60ljnGlnbbJJN8IDSiAfjoUvI9B-qF5@chimpanzee.rmq.cloudamqp.com/wektanqn",
    result_backend="amqps://wektanqn:Q60ljnGlnbbJJN8IDSiAfjoUvI9B-qF5@chimpanzee.rmq.cloudamqp.com/wektanqn",
)
celery_app.config_from_object(settings, namespace="CELERY")
celery_app.conf.update(
    BROKER_URL="amqps://wektanqn:Q60ljnGlnbbJJN8IDSiAfjoUvI9B-qF5@chimpanzee.rmq.cloudamqp.com/wektanqn",
    CELERY_RESULT_BACKEND="amqps://wektanqn:Q60ljnGlnbbJJN8IDSiAfjoUvI9B-qF5@chimpanzee.rmq.cloudamqp.com/wektanqn",
    BROKER_POOL_LIMIT=1,
)
celery_app.conf.beat_schedule = {
    "appointments_update_task": {
        "task": "booking.tasks.appointments_update",
        "schedule": 5,
    },
}

celery_app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


@celery_app.task(bind=True)
def debug_task(self):
    print("Request: {0!r}".format(self.request))
