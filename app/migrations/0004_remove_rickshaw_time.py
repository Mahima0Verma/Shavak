# Generated by Django 4.0.5 on 2022-09-24 18:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_bus_book_now'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rickshaw',
            name='time',
        ),
    ]
