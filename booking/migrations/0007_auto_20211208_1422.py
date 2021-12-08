# Generated by Django 3.2.9 on 2021-12-08 19:22

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("booking", "0006_auto_20211208_1357"),
    ]

    operations = [
        migrations.AlterField(
            model_name="appointment",
            name="end_time",
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name="appointment",
            name="start_time",
            field=models.TimeField(
                validators=[
                    django.core.validators.MinValueValidator(
                        limit_value=datetime.time(14, 22, 31, 972039)
                    )
                ]
            ),
        ),
        migrations.AlterField(
            model_name="appointment",
            name="status",
            field=models.CharField(
                choices=[
                    ("active", "active"),
                    ("cancelled", "cancelled"),
                    ("expired", "expired"),
                ],
                default="active",
                max_length=10,
            ),
        ),
    ]