# Generated by Django 2.0.6 on 2018-12-15 12:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vlog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='vlog',
            options={'ordering': ('-created',), 'verbose_name_plural': '视频'},
        ),
    ]
