# Generated by Django 4.2.7 on 2023-12-26 15:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proj', '0010_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='busprofile',
            name='email',
        ),
        migrations.RemoveField(
            model_name='busprofile',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='busprofile',
            name='last_name',
        ),
    ]
