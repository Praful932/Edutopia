# Generated by Django 3.0 on 2019-12-13 10:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0008_auto_20191212_2040"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="location",
        ),
    ]
