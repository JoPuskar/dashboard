# Generated by Django 2.0 on 2018-11-15 15:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('visualizations', '0053_auto_20181115_1947'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recentstories',
            name='banner',
        ),
    ]
