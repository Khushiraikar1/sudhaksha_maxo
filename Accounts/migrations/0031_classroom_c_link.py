# Generated by Django 3.1.3 on 2021-01-10 02:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0030_posts_posted_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='classroom',
            name='c_link',
            field=models.URLField(default=None, null=True),
        ),
    ]