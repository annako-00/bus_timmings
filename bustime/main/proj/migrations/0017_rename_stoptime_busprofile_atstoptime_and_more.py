# Generated by Django 4.2.7 on 2023-12-26 16:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proj', '0016_busprofile_stoptime'),
    ]

    operations = [
        migrations.RenameField(
            model_name='busprofile',
            old_name='stoptime',
            new_name='atstoptime',
        ),
        migrations.RenameField(
            model_name='busprofile',
            old_name='usstopname',
            new_name='ststopname',
        ),
    ]
