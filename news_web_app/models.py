from django.db import models

class NewsItem(models.Model):
    source = models.CharField(max_length=200, null=True)
    author = models.CharField(max_length=200, null=True)
    title = models.CharField(max_length=200, null=True)
    description = models.TextField()
    url = models.URLField()
    image_url = models.URLField()
    published_at = models.DateTimeField()
    content = models.TextField()
