# Generated by Django 2.2.13 on 2021-03-23 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendors', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendor',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
