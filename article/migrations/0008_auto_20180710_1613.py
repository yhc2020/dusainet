# Generated by Django 2.0.6 on 2018-07-10 08:13

from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0007_auto_20180710_1129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlespost',
            name='column',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='column', to='article.ArticlesColumn'),
        ),
        migrations.AlterField(
            model_name='articlespost',
            name='tags',
            field=taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]
