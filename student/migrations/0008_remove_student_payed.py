# Generated by Django 4.0 on 2022-02-09 13:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0007_pays_student_payed_pays_s_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='payed',
        ),
    ]
