# Generated by Django 4.2.20 on 2025-03-28 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0009_alter_user_a_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='laptop',
            name='status',
            field=models.CharField(default='Checked In', max_length=20),
        ),
    ]
