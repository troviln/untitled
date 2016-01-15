from django.db import models
from django.utils import timezone
from django.db import models
from embed_video.fields import EmbedVideoField


class Tag(models.Model):
    tag = models.CharField(unique=True, max_length=30, blank=True, null=True)

    def __str__(self):
        return self.tag


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    image = models.ImageField(upload_to='images/', height_field=None, width_field=None, max_length=100, blank=True,
                              null=True)
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)
    likes = models.IntegerField(default=0)
    video = EmbedVideoField(blank=True, null=True)  # same like models.URLField()
    tags = models.ManyToManyField(Tag, )

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def approved_comments(self):
        return self.comments.filter(approved_comment=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey('blog.Post', related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField(verbose_name='Comment', max_length=500)
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text


class Chat(models.Model):
    author = models.ForeignKey('auth.User')
    text = models.TextField(verbose_name='message', max_length=200)
    created_date = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.text
