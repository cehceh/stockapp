# Generated by Django 2.2.13 on 2021-02-15 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='is_client',
            field=models.BooleanField(default=True),
        ),
    ]
