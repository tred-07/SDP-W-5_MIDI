# Generated by Django 5.1.3 on 2024-11-19 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0003_alter_comment_car'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
