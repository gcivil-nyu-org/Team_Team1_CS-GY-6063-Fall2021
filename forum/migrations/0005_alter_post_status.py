# Generated by Django 3.2.7 on 2021-11-03 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("forum", "0004_alter_post_status"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="status",
            field=models.CharField(
                choices=[("published", "published"), ("draft", "draft")],
                default="draft",
                max_length=10,
            ),
        ),
    ]
