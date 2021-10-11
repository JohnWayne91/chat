from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Posts(models.Model):
    title = models.CharField(max_length=255, verbose_name='Title')
    slug = models.SlugField(unique=True)
    content = models.TextField(verbose_name='Post content')
    created_at = models.DateTimeField(auto_now=True, verbose_name='Created at')

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    def __str__(self):
        return str(self.id)


class Comment(models.Model):
    author = models.ForeignKey(User, verbose_name='Author', on_delete=models.CASCADE)
    text = models.TextField(verbose_name='Comment text')
    related_post = models.ForeignKey(Posts, verbose_name='Related post', on_delete=models.CASCADE, related_name='post')
    comment_time = models.DateTimeField(null=True, verbose_name='Sending time', default=None)

    def __str__(self):
        return self.text
