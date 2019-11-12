from django.db import models

# Create your models here.
class Post(models.Model):
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=500)
    body = models.TextField(max_length=1000)

    def __str__(self):
        return self.title


class Comment(models.Model):
    author = models.CharField(max_length=100)
    body = models.CharField(max_length=500)
    # preview_url = models.TextField(null=True, blank=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return self.author


# class Favorite(models.Model):
#     user = models.ForeignKey('auth.User', related_name='favorites', on_delete=models.CASCADE)
#     post = models.ForeignKey(Post, related_name='favorites', on_delete=models.CASCADE)