# Generated by Django 4.2.5 on 2023-10-29 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("addBlog", "0004_alter_blog_author_alter_blog_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="blog", name="dislikes", field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="blog", name="likes", field=models.IntegerField(default=0),
        ),
    ]