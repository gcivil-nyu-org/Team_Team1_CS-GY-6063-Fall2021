# Generated by Django 3.2.10 on 2021-12-14 22:40

import datetime
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(validators=[django.core.validators.MinValueValidator(limit_value=datetime.date(2021, 12, 14))])),
                ('start_time', models.TimeField(validators=[django.core.validators.MinValueValidator(limit_value=datetime.time(17, 40, 21, 8668))])),
                ('end_time', models.TimeField()),
                ('meeting_link', models.URLField(blank=True)),
                ('status', models.CharField(choices=[('cancelled', 'cancelled'), ('expired', 'expired'), ('active', 'active')], default='active', max_length=10)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='doctor', to=settings.AUTH_USER_MODEL)),
                ('patient', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='patient', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
