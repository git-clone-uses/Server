# Generated by Django 2.1.1 on 2018-11-20 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0009_incoming_data_server_date_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='object',
            name='Gos_Nomer',
            field=models.CharField(max_length=9),
        ),
    ]
