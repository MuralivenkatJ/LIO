# Generated by Django 4.0 on 2022-01-17 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0004_rates_desc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enrolls',
            name='status',
            field=models.CharField(default='inprogress', max_length=30),
        ),
    ]
