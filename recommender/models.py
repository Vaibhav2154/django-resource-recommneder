from django.db import models

class Interest(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Resource(models.Model):
    TYPE_CHOICES = [
        ('video', 'YouTube Video'),
        ('podcast', 'Spotify Podcast'),
        ('blog', 'Blog'),
    ]
    title = models.CharField(max_length=255)
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    content = models.TextField()
    url = models.URLField()
    similarity_score = models.FloatField(default=0.0)

    def __str__(self):
        return f"{self.title} ({self.type})"
