# Generated by Django 4.0.3 on 2022-09-23 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_rename_destination_bus_route_remove_bus_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bus',
            name='Book_Now',
            field=models.CharField(max_length=100),
        ),
    ]