# Generated by Django 4.0 on 2022-01-16 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0010_alter_course_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='image',
            field=models.ImageField(upload_to='course'),
        ),
    ]