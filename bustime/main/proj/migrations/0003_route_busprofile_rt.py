# Generated by Django 4.2.7 on 2023-12-20 11:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('proj', '0002_rename_name_busprofile_fname_busprofile_lname_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Route',
            fields=[
                ('route', models.CharField(max_length=100, primary_key=True, serialize=False)),
            ],
        ),
        migrations.AddField(
            model_name='busprofile',
            name='rt',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='proj.route'),
        ),
    ]
