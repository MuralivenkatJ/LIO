# Generated by Django 4.0 on 2022-01-16 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0009_course_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='description',
            field=models.CharField(max_length=600),
        ),
    ]