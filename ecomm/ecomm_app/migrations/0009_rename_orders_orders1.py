# Generated by Django 5.1.3 on 2024-11-21 08:27

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecomm_app', '0008_orders'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='orders',
            new_name='orders1',
        ),
    ]
