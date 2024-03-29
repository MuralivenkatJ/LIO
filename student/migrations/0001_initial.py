# Generated by Django 4.0 on 2022-01-15 09:45

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('institute', '0001_initial'),
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Enrolls',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=30)),
                ('c_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.course')),
            ],
        ),
        migrations.CreateModel(
            name='Rates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(0)])),
                ('c_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.course')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('s_id', models.IntegerField(primary_key=True, serialize=False)),
                ('s_name', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=200)),
                ('courses', models.ManyToManyField(related_name='courses', through='student.Enrolls', to='course.Course')),
                ('i_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='institute.institute')),
                ('ratings', models.ManyToManyField(related_name='ratings', through='student.Rates', to='course.Course')),
            ],
        ),
        migrations.CreateModel(
            name='Wishlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.course')),
                ('s_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.student')),
            ],
            options={
                'unique_together': {('s_id', 'c_id')},
            },
        ),
        migrations.AddField(
            model_name='student',
            name='wished',
            field=models.ManyToManyField(related_name='wished', through='student.Wishlist', to='course.Course'),
        ),
        migrations.AddField(
            model_name='rates',
            name='s_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.student'),
        ),
        migrations.AddField(
            model_name='enrolls',
            name='s_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.student'),
        ),
        migrations.AlterUniqueTogether(
            name='rates',
            unique_together={('s_id', 'c_id')},
        ),
        migrations.AlterUniqueTogether(
            name='enrolls',
            unique_together={('s_id', 'c_id')},
        ),
    ]
