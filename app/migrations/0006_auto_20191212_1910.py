# Generated by Django 3.0 on 2019-12-12 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0005_auto_20191210_1904"),
    ]

    operations = [
        migrations.AlterField(
            model_name="mentor",
            name="OtherInfo",
            field=models.TextField(
                help_text="Your Github/Portfolio Page or Anything you would like to add",
                max_length=200,
                null=True,
            ),
        ),
    ]
