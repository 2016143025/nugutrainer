# Generated by Django 4.1 on 2022-09-10 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("nuguhome", "0006_gymlocation_delete_gym_location"),
    ]

    operations = [
        migrations.AddField(
            model_name="trainer",
            name="starsocre",
            field=models.IntegerField(default=0),
        ),
    ]