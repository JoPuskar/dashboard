# Generated by Django 2.0 on 2018-11-15 07:19

from django.db import migrations
import stdimage.models
import stdimage.validators


class Migration(migrations.Migration):

    dependencies = [
        ('visualizations', '0050_auto_20181115_1250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recentstories',
            name='banner',
            field=stdimage.models.StdImageField(upload_to='', validators=[stdimage.validators.MinSizeValidator(1600, 600)]),
        ),
    ]
