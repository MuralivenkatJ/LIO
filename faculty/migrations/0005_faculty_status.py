# Generated by Django 4.0 on 2022-03-28 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faculty', '0004_alter_faculty_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='faculty',
            name='status',
            field=models.CharField(default='Pending', max_length=30),
        ),
    ]
