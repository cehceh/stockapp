# Generated by Django 2.2.13 on 2021-04-25 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_auto_20210425_0044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='barimg',
            field=models.ImageField(blank=True, null=True, upload_to='barcodes'),
        ),
    ]