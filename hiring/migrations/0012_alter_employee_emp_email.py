# Generated by Django 4.0.4 on 2022-05-27 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hiring', '0011_rename_job_sub_title_jobapplication_job_app_sub_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='emp_email',
            field=models.EmailField(max_length=100, unique=True),
        ),
    ]
