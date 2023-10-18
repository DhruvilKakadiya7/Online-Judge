# Generated by Django 4.2.6 on 2023-10-18 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('problemPage', '0004_alter_submission_language'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='language',
            field=models.CharField(choices=[('c++', 'cpp'), ('python', 'Python'), ('java', 'Java')], default='c++', max_length=50),
        ),
        migrations.AlterField(
            model_name='submission',
            name='verdict',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
