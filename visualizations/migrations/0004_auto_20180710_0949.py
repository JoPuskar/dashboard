# Generated by Django 2.0 on 2018-07-10 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visualizations', '0003_auto_20180706_0728'),
    ]

    operations = [
        migrations.AddField(
            model_name='data',
            name='houses_completed',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='data',
            name='number_of_women',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='data',
            name='total_houses',
            field=models.IntegerField(default=0),
        ),
    ]
