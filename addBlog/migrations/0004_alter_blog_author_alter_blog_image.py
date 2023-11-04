# Generated by Django 4.2.5 on 2023-10-29 18:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("addBlog", "0003_remove_blog_username_blog_author"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blog",
            name="author",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AlterField(
            model_name="blog",
            name="image",
            field=models.ImageField(upload_to="media/blog_image"),
        ),
    ]
