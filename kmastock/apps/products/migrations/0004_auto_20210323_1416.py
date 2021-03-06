# Generated by Django 2.2.13 on 2021-03-23 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_product_updateduser'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='title',
        ),
        migrations.AddField(
            model_name='product',
            name='barcode',
            field=models.CharField(blank=True, max_length=120, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='product',
            name='originprice',
            field=models.DecimalField(decimal_places=2, default=39.99, max_digits=20),
        ),
    ]
