# Generated by Django 2.2.13 on 2021-03-23 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0003_auto_20210323_0911'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categories',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
