# Generated by Django 2.1.3 on 2018-11-26 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wagtail_calendar', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateTimeField(verbose_name='Event date'),
        ),
    ]