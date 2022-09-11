# Generated by Django 4.1 on 2022-09-11 07:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("nuguhome", "0015_delete_score"),
    ]

    operations = [
        migrations.CreateModel(
            name="score",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("score", models.IntegerField(default=10)),
                (
                    "trainer_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="nuguhome.trainer",
                    ),
                ),
            ],
        ),
    ]
