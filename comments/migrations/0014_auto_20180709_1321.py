# Generated by Django 2.0.6 on 2018-07-09 05:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0013_albumcomment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='albumcomment',
            name='level',
        ),
        migrations.RemoveField(
            model_name='albumcomment',
            name='lft',
        ),
        migrations.RemoveField(
            model_name='albumcomment',
            name='parent',
        ),
        migrations.RemoveField(
            model_name='albumcomment',
            name='reply_to',
        ),
        migrations.RemoveField(
            model_name='albumcomment',
            name='rght',
        ),
        migrations.RemoveField(
            model_name='albumcomment',
            name='tree_id',
        ),
    ]
