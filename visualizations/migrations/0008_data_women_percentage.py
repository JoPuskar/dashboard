# Generated by Django 2.0 on 2018-07-11 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visualizations', '0007_remove_data_women_percentange'),
    ]

    operations = [
        migrations.AddField(
            model_name='data',
            name='women_percentage',
            field=models.IntegerField(default=0),
        ),
    ]
