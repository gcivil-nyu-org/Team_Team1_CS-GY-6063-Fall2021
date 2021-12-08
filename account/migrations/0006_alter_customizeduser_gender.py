# Generated by Django 3.2.9 on 2021-12-08 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_alter_customizeduser_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customizeduser',
            name='gender',
            field=models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female')], max_length=1),
        ),
    ]
