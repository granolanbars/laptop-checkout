# Generated by Django 4.2.20 on 2025-03-25 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='laptop',
            name='status',
            field=models.CharField(choices=[('checked_out', 'Checked Out'), ('checked_in', 'Checked In')], default='checked_in', max_length=20),
        ),
    ]
