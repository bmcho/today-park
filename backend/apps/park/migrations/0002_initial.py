# Generated by Django 4.0 on 2022-01-03 16:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("park", "0001_initial"),
        ("user", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="review",
            name="user_id",
            field=models.ForeignKey(
                db_column="user_id",
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="review_user",
                to="user.user",
                verbose_name="유저 ID",
            ),
        ),
        migrations.AddField(
            model_name="parkequipment",
            name="equipment_id",
            field=models.ForeignKey(
                db_column="equipment_id",
                on_delete=django.db.models.deletion.CASCADE,
                related_name="equipment",
                to="park.equipment",
                verbose_name="운동시설 ID",
            ),
        ),
        migrations.AddField(
            model_name="parkequipment",
            name="park_id",
            field=models.ForeignKey(
                db_column="park_id",
                on_delete=django.db.models.deletion.CASCADE,
                related_name="park",
                to="park.park",
                verbose_name="공원 ID",
            ),
        ),
    ]
