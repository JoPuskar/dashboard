# Generated by Django 2.0 on 2018-07-19 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visualizations', '0008_data_women_percentage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='district',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
