# Generated by Django 4.2.7 on 2024-01-06 11:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('proj', '0029_rename_stopname_busprofile_endstopname_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Article',
        ),
        migrations.AlterField(
            model_name='busprofile',
            name='ststopname',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='proj.stopname'),
        ),
    ]
