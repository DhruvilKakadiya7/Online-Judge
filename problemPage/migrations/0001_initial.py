# Generated by Django 4.2.6 on 2023-10-16 03:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TestCases',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('input_text', models.TextField()),
                ('output_text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('statement', models.TextField()),
                ('input_description', models.TextField()),
                ('output_description', models.TextField()),
                ('explanation', models.TextField()),
                ('testcases', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='problemPage.testcases')),
            ],
        ),
    ]
