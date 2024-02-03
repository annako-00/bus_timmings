# Generated by Django 4.2.7 on 2023-12-20 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proj', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='busprofile',
            old_name='name',
            new_name='fname',
        ),
        migrations.AddField(
            model_name='busprofile',
            name='lname',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='busprofile',
            name='pass1',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='busprofile',
            name='bio',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
