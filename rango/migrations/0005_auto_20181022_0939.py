# Generated by Django 2.1.1 on 2018-10-22 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0004_auto_20181022_0917'),
    ]

    operations = [
        migrations.AddField(
            model_name='incoming_data',
            name='adc',
            field=models.CharField(default='NA', max_length=256),
        ),
        migrations.AddField(
            model_name='incoming_data',
            name='hdops',
            field=models.CharField(default='NA', max_length=256),
        ),
        migrations.AddField(
            model_name='incoming_data',
            name='ibutton',
            field=models.CharField(default='NA', max_length=256),
        ),
        migrations.AddField(
            model_name='incoming_data',
            name='inputs',
            field=models.CharField(default='NA', max_length=256),
        ),
        migrations.AddField(
            model_name='incoming_data',
            name='outputs',
            field=models.CharField(default='NA', max_length=256),
        ),
        migrations.AddField(
            model_name='incoming_data',
            name='params',
            field=models.CharField(default='NA', max_length=256),
        ),
    ]
