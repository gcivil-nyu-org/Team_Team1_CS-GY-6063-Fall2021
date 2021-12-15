web: gunicorn VMentalHealth.wsgi

worker: celery worker --app=booking.tasks.appointments_update -B -E -l info