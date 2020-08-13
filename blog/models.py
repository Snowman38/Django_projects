
from django.conf import settings
from django.utils import timezone
from django.db import models


class Post(models.Model):
    image = models.ImageField(upload_to='post_images/', null=True, blank=True)
    slug = models.SlugField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)


class Comment(models.Model):
    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=20)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def publish(self):
        self.published_date = timezone.now()
        self.save

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text


class Project(models.Model):
    image = models.ImageField(upload_to='project_images/', null=True, blank=True)
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    short_text = models.TextField(max_length=130)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
