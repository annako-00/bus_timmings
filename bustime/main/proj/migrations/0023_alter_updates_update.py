# Generated by Django 4.2.7 on 2023-12-29 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proj', '0022_updates'),
    ]

    operations = [
        migrations.AlterField(
            model_name='updates',
            name='update',
            field=models.TextField(max_length=200),
        ),
    ]