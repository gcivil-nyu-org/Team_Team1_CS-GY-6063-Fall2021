from __future__ import absolute_import, unicode_literals

import os

from celery import Celery

from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "VMentalHealth.settings")

celery_app = Celery(
    "VMentalHealth",
    broker="amqps://fgmleaxv:TsAnfCqlAeSAjRHbYXmWKrKe8RfoI5R-@fox.rmq.cloudamqp.com/fgmleaxv",
    result_backend="amqps://fgmleaxv:TsAnfCqlAeSAjRHbYXmWKrKe8RfoI5R-@fox.rmq.cloudamqp.com/fgmleaxv",
)
celery_app.config_from_object(settings, namespace="CELERY")
celery_app.conf.update(
    BROKER_URL="amqps://fgmleaxv:TsAnfCqlAeSAjRHbYXmWKrKe8RfoI5R-@fox.rmq.cloudamqp.com/fgmleaxv",
    CELERY_RESULT_BACKEND="amqps://fgmleaxv:TsAnfCqlAeSAjRHbYXmWKrKe8RfoI5R-@fox.rmq.cloudamqp.com/fgmleaxv",
)
celery_app.conf.beat_schedule = {
    "appointments_update_task": {
        "task": "booking.tasks.appointments_update",
        "schedule": 5,
    },
}

celery_app.autodiscover_tasks()


@celery_app.task(bind=True)
def debug_task(self):
    print("Request: {0!r}".format(self.request))
