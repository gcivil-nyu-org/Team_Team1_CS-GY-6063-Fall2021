# Generated by Django 3.2.8 on 2021-12-08 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0009_alter_appointment_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='status',
            field=models.CharField(choices=[('cancelled', 'cancelled'), ('active', 'active')], default='active', max_length=10),
        ),
    ]
