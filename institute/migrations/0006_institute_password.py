# Generated by Django 4.0 on 2022-02-09 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('institute', '0005_remove_institute_b_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='institute',
            name='password',
            field=models.CharField(default='e10adc3949ba59abbe56e057f20f883e', max_length=200),
            preserve_default=False,
        ),
    ]
