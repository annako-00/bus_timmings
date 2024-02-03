# Generated by Django 4.2.7 on 2024-01-06 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proj', '0028_rename_endstopname_busprofile_stopname_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='busprofile',
            old_name='stopname',
            new_name='endstopname',
        ),
        migrations.AddField(
            model_name='busprofile',
            name='stop2name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='busprofile',
            name='stop3name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='busprofile',
            name='stop4name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='busprofile',
            name='stop5name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='busprofile',
            name='stop6name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='busprofile',
            name='ststopname',
            field=models.CharField(max_length=100, null=True),
        ),
    ]