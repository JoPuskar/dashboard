# Generated by Django 2.0.7 on 2018-07-24 05:07

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('visualizations', '0009_auto_20180719_1216'),
    ]

    operations = [
        migrations.CreateModel(
            name='RecentStories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20, verbose_name='Title')),
                ('description', models.CharField(max_length=20, verbose_name='Short Description')),
            ],
        ),
    ]
