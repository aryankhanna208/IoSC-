# Generated by Django 4.1.7 on 2023-08-20 13:04

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_rename_program_user_branch'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='enrollment_no',
            field=models.BigIntegerField(unique=True, validators=[django.core.validators.MaxValueValidator(9999999999), django.core.validators.MinValueValidator(10000000000)]),
        ),
    ]