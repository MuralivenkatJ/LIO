# Generated by Django 4.0 on 2022-01-25 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0012_course_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='no_videos',
            field=models.IntegerField(default=0),
        ),
    ]
