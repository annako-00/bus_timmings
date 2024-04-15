# Generated by Django 4.2.7 on 2024-01-06 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proj', '0026_alter_busprofile_ststopname'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('bno', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('bname', models.CharField(max_length=100, null=True)),
                ('username', models.CharField(max_length=50)),
                ('bio', models.CharField(max_length=100, null=True)),
                ('phno', models.IntegerField()),
                ('stoptime', models.CharField(max_length=100, null=True)),
                ('stop2time', models.CharField(max_length=100, null=True)),
                ('stop3time', models.CharField(max_length=100, null=True)),
                ('stop4time', models.CharField(max_length=100, null=True)),
                ('stop5time', models.CharField(max_length=100, null=True)),
                ('stop6time', models.CharField(max_length=100, null=True)),
                ('stopname', models.CharField(max_length=100, null=True)),
                ('endstoptime', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]
