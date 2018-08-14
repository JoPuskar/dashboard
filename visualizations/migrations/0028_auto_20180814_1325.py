# Generated by Django 2.0 on 2018-08-14 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visualizations', '0027_aboutus'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='aboutus',
            options={'verbose_name_plural': 'About Us'},
        ),
        migrations.AddField(
            model_name='projectstakeholders',
            name='name',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='projectstakeholders',
            name='role',
            field=models.TextField(blank=True, null=True),
        ),
    ]
