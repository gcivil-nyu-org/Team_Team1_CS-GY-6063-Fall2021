# Generated by Django 3.2.7 on 2021-10-27 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("vmental", "0009_merge_20211027_1423"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customizeduser",
            name="gender",
            field=models.CharField(
                blank=True, choices=[("M", "Male"), ("F", "Female")], max_length=1
            ),
        ),
    ]
