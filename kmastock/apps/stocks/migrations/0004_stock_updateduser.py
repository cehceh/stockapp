# Generated by Django 2.2.13 on 2021-03-23 10:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('stocks', '0003_auto_20210323_0930'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='updateduser',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_make_stock_changes', to=settings.AUTH_USER_MODEL),
        ),
    ]
