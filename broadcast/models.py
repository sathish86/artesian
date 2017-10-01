from django.db import models
from django.contrib.auth.models import User


class PostManager(models.Manager):
    def get_queryset(self):
        return super(PostManager, self).get_queryset().order_by('-updated')


# Create your models here.
class Post(models.Model):
    post = models.CharField(max_length=400)
    user = models.ForeignKey(User)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects = models.Manager()  # The default manager.
    latest_post = PostManager()  # PostManger class.
