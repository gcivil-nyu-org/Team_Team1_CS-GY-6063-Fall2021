# Generated by Django 3.2.8 on 2021-11-09 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0005_alter_appointments_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointments',
            name='status',
            field=models.CharField(choices=[('confirmed', 'confirmed'), ('available', 'available')], default='available', max_length=10),
        ),
    ]
