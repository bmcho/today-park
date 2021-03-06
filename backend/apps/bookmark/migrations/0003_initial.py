# Generated by Django 4.0 on 2022-01-03 16:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("bookmark", "0002_initial"),
        ("user", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="bookmark",
            name="user_id",
            field=models.ForeignKey(
                db_column="user_id",
                on_delete=django.db.models.deletion.CASCADE,
                related_name="bookmark_user",
                to="user.user",
                verbose_name="유저 ID",
            ),
        ),
    ]
