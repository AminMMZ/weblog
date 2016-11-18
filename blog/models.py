from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(User)
    date = models.DateTimeField(default = timezone.now)
    title = models.CharField(max_length = 100)
    text = models.TextField()
    def __unicode__(self):
        return self.title
class Comment(models.Model):
    post = models.ForeignKey(Post)
    name = models.CharField(max_length = 100)
    text = models.TextField()
    date = models.DateTimeField(default = timezone.now)