# Generated by Django 4.0 on 2022-01-15 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='c_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='course_skills',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
