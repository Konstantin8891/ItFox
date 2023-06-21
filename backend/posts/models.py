from django.db import models

from users.models import Users


class News(models.Model):
    title = models.CharField(max_length=200, unique=True)
    text = models.TextField()
    likes = models.IntegerField(default=0)
    author = models.ForeignKey(
        Users, related_name='news_author', on_delete=models.CASCADE
    )
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Новости"

    def __str__(self):
        return self.title


class Comments(models.Model):
    text = models.TextField()
    post_id = models.ForeignKey(
        News, related_name='comments', on_delete=models.CASCADE
    )
    author_id = models.ForeignKey(
        Users, related_name='comments', on_delete=models.CASCADE
    )
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Коментарии"
