# Generated by Django 4.0.4 on 2022-05-27 03:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hiring', '0006_remove_jobapplicant_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobapplicant',
            name='job_appl_app_id',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='hiring.jobapplication'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='jobapplicant',
            name='job_appl_status',
            field=models.CharField(choices=[('APPLIED', 'APPLIED'), ('PENDING', 'PENDING'), ('APPROVED', 'APPROVED'), ('SCHEDULED', 'SCHEDULED'), ('INTERVIEWED', 'INTERVIEWED'), ('SELECTED', 'SELECTED'), ('ACCEPTED', 'ACCEPTED'), ('REJECTED', 'REJECTED')], default='APPLIED', max_length=100),
        ),
    ]
