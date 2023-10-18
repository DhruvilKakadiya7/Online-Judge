# Generated by Django 4.2.6 on 2023-10-18 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('problemPage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('problem_id', models.IntegerField()),
                ('user_id', models.IntegerField()),
                ('submission_time', models.DateTimeField()),
                ('language', models.CharField(max_length=50)),
                ('verdict', models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='Problem',
        ),
        migrations.DeleteModel(
            name='TestCases',
        ),
    ]
