# Generated by Django 4.2.6 on 2023-10-21 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('problemPage', '0008_testcaseresult_user_output'),
    ]

    operations = [
        migrations.AddField(
            model_name='testcaseresult',
            name='problem_tc_id',
            field=models.IntegerField(default=-1),
        ),
    ]
