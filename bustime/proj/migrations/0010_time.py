# Generated by Django 4.2.7 on 2023-12-26 15:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('proj', '0009_busprofile'),
    ]

    operations = [
        migrations.CreateModel(
            name='time',
            fields=[
                ('stopname', models.CharField(max_length=100)),
                ('time', models.CharField(max_length=100)),
                ('busname', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('busno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proj.busprofile')),
            ],
        ),
    ]
