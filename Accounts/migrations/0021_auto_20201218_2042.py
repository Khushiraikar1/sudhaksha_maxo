# Generated by Django 3.1.3 on 2020-12-18 20:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0020_auto_20201218_1916'),
    ]

    operations = [
        migrations.RenameField(
            model_name='timetable',
            old_name='lass_obj',
            new_name='clsobj',
        ),
    ]
