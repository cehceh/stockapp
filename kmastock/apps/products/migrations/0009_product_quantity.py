# Generated by Django 2.2.13 on 2021-04-29 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_auto_20210425_1542'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='quantity',
            field=models.CharField(default='', max_length=20),
        ),
    ]
