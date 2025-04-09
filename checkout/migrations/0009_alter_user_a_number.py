# Generated by Django 4.2.20 on 2025-03-28 15:44

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0008_rename_user_id_laptop_checkout_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='a_number',
            field=models.CharField(max_length=9, primary_key=True, serialize=False, unique=True, validators=[django.core.validators.RegexValidator('^[Aa]\\d{8}$', message='Invalid A number format')], verbose_name='Anumber'),
        ),
    ]
