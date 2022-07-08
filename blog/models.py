from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=250)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title
