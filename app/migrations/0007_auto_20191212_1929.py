# Generated by Django 3.0 on 2019-12-12 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0006_auto_20191212_1910"),
    ]

    operations = [
        migrations.AlterField(
            model_name="domain",
            name="description",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="domain",
            name="domaintrack",
            field=models.URLField(),
        ),
        migrations.AlterField(
            model_name="mentor",
            name="OtherInfo",
            field=models.TextField(
                help_text="Your Github/Portfolio Page or Anything you would like to add",
                max_length=200,
            ),
        ),
        migrations.AlterField(
            model_name="post",
            name="content",
            field=models.TextField(max_length=1000),
        ),
    ]
