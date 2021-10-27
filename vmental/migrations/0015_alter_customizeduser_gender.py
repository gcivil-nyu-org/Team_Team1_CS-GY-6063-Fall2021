# Generated by Django 3.2.8 on 2021-10-27 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vmental', '0014_alter_customizeduser_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customizeduser',
            name='gender',
            field=models.CharField(blank=True, choices=[('F', 'Female'), ('M', 'Male')], max_length=1),
        ),
    ]