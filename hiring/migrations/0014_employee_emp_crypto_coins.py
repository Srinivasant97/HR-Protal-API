# Generated by Django 4.0.4 on 2022-05-28 23:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hiring', '0013_alter_applicant_apl_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='emp_crypto_coins',
            field=models.IntegerField(default=0),
        ),
    ]
