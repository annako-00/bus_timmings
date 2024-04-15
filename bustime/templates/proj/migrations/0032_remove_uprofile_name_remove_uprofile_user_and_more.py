# Generated by Django 4.2.7 on 2024-01-07 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proj', '0031_alter_busprofile_ststopname'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='uprofile',
            name='name',
        ),
        migrations.RemoveField(
            model_name='uprofile',
            name='user',
        ),
        migrations.AddField(
            model_name='uprofile',
            name='firstname',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='uprofile',
            name='lastname',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='uprofile',
            name='password1',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='uprofile',
            name='username',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='uprofile',
            name='bio',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='uprofile',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='uprofile',
            name='phno',
            field=models.IntegerField(null=True),
        ),
    ]
