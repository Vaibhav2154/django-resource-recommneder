# Generated by Django 5.1.5 on 2025-01-18 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Interest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('type', models.CharField(choices=[('video', 'YouTube Video'), ('podcast', 'Spotify Podcast'), ('blog', 'Blog')], max_length=20)),
                ('content', models.TextField()),
                ('url', models.URLField()),
                ('similarity_score', models.FloatField(default=0.0)),
            ],
        ),
    ]
