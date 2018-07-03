# Generated by Django 2.0.6 on 2018-07-03 08:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0010_auto_20180703_1605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='reply_to',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reply_to', to=settings.AUTH_USER_MODEL),
        ),
    ]
