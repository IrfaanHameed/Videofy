# Generated by Django 4.2.13 on 2024-06-26 03:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0002_video_video_url_alter_video_video_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='video_file',
        ),
    ]
