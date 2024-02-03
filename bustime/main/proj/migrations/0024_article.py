# Generated by Django 4.2.7 on 2024-01-05 15:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('proj', '0023_alter_updates_update'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('bno', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('bname', models.CharField(max_length=100, null=True)),
                ('bio', models.CharField(max_length=100, null=True)),
                ('ststoptime', models.CharField(max_length=100, null=True)),
                ('stop2name', models.CharField(max_length=100, null=True)),
                ('stop2time', models.CharField(max_length=100, null=True)),
                ('stop3name', models.CharField(max_length=100, null=True)),
                ('stop3time', models.CharField(max_length=100, null=True)),
                ('stop4name', models.CharField(max_length=100, null=True)),
                ('stop4time', models.CharField(max_length=100, null=True)),
                ('stop5name', models.CharField(max_length=100, null=True)),
                ('stop5time', models.CharField(max_length=100, null=True)),
                ('stop6name', models.CharField(max_length=100, null=True)),
                ('stop6time', models.CharField(max_length=100, null=True)),
                ('endstopname', models.CharField(max_length=100, null=True)),
                ('endstoptime', models.CharField(max_length=100, null=True)),
                ('ststopname', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='proj.stopname')),
            ],
        ),
    ]