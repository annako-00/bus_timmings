# Generated by Django 4.2.7 on 2024-01-06 11:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proj', '0027_article'),
    ]

    operations = [
        migrations.RenameField(
            model_name='busprofile',
            old_name='endstopname',
            new_name='stopname',
        ),
        migrations.RemoveField(
            model_name='busprofile',
            name='stop2name',
        ),
        migrations.RemoveField(
            model_name='busprofile',
            name='stop3name',
        ),
        migrations.RemoveField(
            model_name='busprofile',
            name='stop4name',
        ),
        migrations.RemoveField(
            model_name='busprofile',
            name='stop5name',
        ),
        migrations.RemoveField(
            model_name='busprofile',
            name='stop6name',
        ),
        migrations.RemoveField(
            model_name='busprofile',
            name='ststopname',
        ),
    ]