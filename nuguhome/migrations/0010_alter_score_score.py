# Generated by Django 4.1 on 2022-09-11 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("nuguhome", "0009_score"),
    ]

    operations = [
        migrations.AlterField(
            model_name="score", name="score", field=models.IntegerField(default=8),
        ),
    ]