# Generated by Django 5.1.3 on 2024-11-18 17:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0002_alter_car_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='slug',
        ),
    ]
