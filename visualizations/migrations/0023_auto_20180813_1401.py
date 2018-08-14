# Generated by Django 2.0 on 2018-08-13 08:16

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('visualizations', '0022_auto_20180813_1207'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dispensedamount',
            options={'verbose_name_plural': 'Dispensed Amount'},
        ),
        migrations.AlterModelOptions(
            name='media',
            options={'verbose_name_plural': 'Media'},
        ),
        migrations.AlterModelOptions(
            name='projectstakeholders',
            options={'verbose_name_plural': 'Project Stakeholders'},
        ),
        migrations.AlterField(
            model_name='dispensedamount',
            name='amount',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='recentstories',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2018, 8, 13, 8, 16, 55, 621407, tzinfo=utc)),
        ),
    ]