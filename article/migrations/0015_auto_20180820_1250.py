# Generated by Django 2.0.6 on 2018-08-20 04:50

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0014_articlespost_course_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlespost',
            name='avatar_thumbnail',
            field=imagekit.models.fields.ProcessedImageField(blank=True, null=True, upload_to='image/article/%Y%m%d'),
        ),
    ]