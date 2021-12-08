# Generated by Django 3.2.9 on 2021-12-08 18:31

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("booking", "0003_alter_appointment_status"),
    ]

    operations = [
        migrations.AlterField(
            model_name="appointment",
            name="date",
            field=models.DateField(
                validators=[
                    django.core.validators.MinValueValidator(
                        limit_value=datetime.date(2021, 12, 7)
                    )
                ]
            ),
        ),
        migrations.AlterField(
            model_name="appointment",
            name="status",
            field=models.CharField(
                choices=[
                    ("cancelled", "cancelled"),
                    ("active", "active"),
                    ("expired", "expired"),
                ],
                default="active",
                max_length=10,
            ),
        ),
    ]