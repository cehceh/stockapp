# Generated by Django 2.2.13 on 2021-03-23 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0002_auto_20210322_1218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]