# Generated by Django 2.0.6 on 2019-01-06 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0026_auto_20190106_1411'),
    ]

    operations = [
        migrations.AddField(
            model_name='readbookcomment',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='readbookcomment',
            name='is_deleted_by_staff',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='vlogcomment',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='vlogcomment',
            name='is_deleted_by_staff',
            field=models.BooleanField(default=False),
        ),
    ]
