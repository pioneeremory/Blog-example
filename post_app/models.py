from django.db import models

# Create your models here.


class Posts(models.Model):
    title = models.CharField(max_length=250)
    post_author = models.CharField()
    date_created = models.DateTimeField(auto_now_add=True)
    body = models.TextField()

    def __str__(self):
        return self.title


class Comments(models.Model):
    text = models.TextField()
    comment_author = models.CharField()
    date_created = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(
        Posts, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return f"({self.comment_author})"
