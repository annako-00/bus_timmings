# Generated by Django 4.2.7 on 2023-12-26 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proj', '0019_rename_atstoptime_busprofile_ststoptime'),
    ]

    operations = [
        migrations.AddField(
            model_name='busprofile',
            name='stop2time',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
