# Generated by Django 4.2.7 on 2023-12-26 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proj', '0020_busprofile_stop2time'),
    ]

    operations = [
        migrations.AddField(
            model_name='busprofile',
            name='stop6name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='busprofile',
            name='stop6time',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
