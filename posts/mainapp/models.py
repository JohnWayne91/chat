from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name='Title')
    slug = models.SlugField(unique=True)
    content = models.TextField(verbose_name='Post content')
    created_at = models.DateTimeField(auto_now=True, verbose_name='Created at')
    comments = models.ManyToManyField('Comments')

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})


class Comments(models.Model):
    author = models.ForeignKey(User, verbose_name='Author', on_delete=models.CASCADE)
    text = models.TextField(verbose_name='Comment text')
    created_at = models.DateTimeField(auto_now_add=True)
    related_post = models.ForeignKey(Post, verbose_name='Related post', on_delete=models.CASCADE, related_name='post')
