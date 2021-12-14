# Generated by Django 3.2.10 on 2021-12-14 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("forum", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="status",
            field=models.CharField(
                choices=[("draft", "draft"), ("published", "published")],
                default="draft",
                max_length=10,
            ),
        ),
    ]
