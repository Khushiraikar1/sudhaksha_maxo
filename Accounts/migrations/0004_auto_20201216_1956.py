# Generated by Django 3.1.3 on 2020-12-16 14:26

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Accounts', '0003_clasroom'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='clasroom',
            new_name='classroom',
        ),
    ]
