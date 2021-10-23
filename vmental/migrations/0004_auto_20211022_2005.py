# Generated by Django 3.2.8 on 2021-10-22 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vmental', '0003_auto_20211022_2002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customizeduser',
            name='gender',
            field=models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female')], max_length=1),
        ),
        migrations.AlterField(
            model_name='customizeduser',
            name='is_provider',
            field=models.BooleanField(default=False),
        ),
    ]