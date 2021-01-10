# Generated by Django 3.1.3 on 2021-01-08 23:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0022_attendance'),
    ]

    operations = [
        migrations.CreateModel(
            name='posts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notes', models.FileField(null=True, upload_to='')),
                ('post', models.TextField(max_length=500, null=True)),
                ('upload_date', models.DateTimeField()),
                ('p_class', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Accounts.classroom')),
            ],
        ),
    ]
