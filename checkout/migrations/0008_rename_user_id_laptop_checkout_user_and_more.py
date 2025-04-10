# Generated by Django 4.2.20 on 2025-03-28 15:36

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0007_alter_transaction_computer_id_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='laptop',
            old_name='user_id',
            new_name='checkout_user',
        ),
        migrations.AlterField(
            model_name='transaction',
            name='computer_id',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='checkout.laptop'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='time_in',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Time In'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='user_id',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='checkout.user'),
        ),
        migrations.AlterField(
            model_name='user',
            name='a_number',
            field=models.CharField(max_length=9, primary_key=True, serialize=False, unique=True, validators=[django.core.validators.RegexValidator('^A\\d{8}$', message='Invalid A number format')], verbose_name='Anumber'),
        ),
    ]
