web: gunicorn VMentalHealth.wsgi

worker: celery worker -B -l info

python manage.py celeryd worker -B -l info