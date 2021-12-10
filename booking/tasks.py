from __future__ import absolute_import, unicode_literals

import datetime

from celery import shared_task

from booking.models import Appointment


@shared_task
def appointments_update():
    Appointment.objects.filter(
        status="active",
        date__range=["2000-01-01", datetime.date.today().strftime("%Y-%m-%d")],
        start_time__range=["00:00:00", datetime.datetime.now().time()],
    ).update(status="expired")
