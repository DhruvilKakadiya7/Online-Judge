# Generated by Django 4.2.5 on 2023-10-28 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("addBlog", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="blog",
            name="username",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
