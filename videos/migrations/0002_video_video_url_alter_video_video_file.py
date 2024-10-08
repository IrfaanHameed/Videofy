# Generated by Django 4.2.13 on 2024-06-26 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='video_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='video',
            name='video_file',
            field=models.FileField(blank=True, null=True, upload_to='videos/'),
        ),
    ]
