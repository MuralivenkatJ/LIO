# Generated by Django 4.0 on 2022-01-15 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0004_course_guided_project'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='total_views',
            field=models.IntegerField(default=0),
        ),
    ]