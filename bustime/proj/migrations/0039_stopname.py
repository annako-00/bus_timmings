# Generated by Django 4.2.7 on 2024-01-15 18:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('proj', '0038_delete_stopname_remove_route_brname_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stopname',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stopname', models.CharField(max_length=100, null=True)),
                ('stoptime', models.CharField(max_length=100, null=True)),
                ('brname', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='proj.busprofile')),
            ],
        ),
    ]
