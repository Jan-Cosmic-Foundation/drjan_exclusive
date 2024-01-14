# Generated by Django 5.0.1 on 2024-01-14 13:19

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, unique=True)),
                ('mini_description', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('thumbnail', models.ImageField(blank=True, upload_to='course_images')),
                ('level', models.CharField(max_length=50)),
                ('core', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lesson_number', models.IntegerField()),
                ('title', models.CharField(max_length=50, unique=True)),
                ('description', models.TextField()),
                ('lesson_type', models.CharField(choices=[('lesson', 'Lesson'), ('supplementary', 'supplementary'), ('q&a', 'Q&A')], default='lesson', max_length=50)),
                ('thumbnail', models.ImageField(blank=True, upload_to='lesson_thumbnails')),
                ('video_source', models.CharField(default='vimeo', max_length=50)),
                ('video_link', models.CharField(max_length=200)),
                ('twi_video_link', models.CharField(blank=True, max_length=200)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lessons', to='exclusive.course')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(blank=True, max_length=20)),
                ('profile_pic', models.ImageField(blank=True, upload_to='profile_pics')),
                ('registered', models.BooleanField(default=False)),
                ('intermediate_access', models.BooleanField(default=False)),
                ('advanced_access', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
