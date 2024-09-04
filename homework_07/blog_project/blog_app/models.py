from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"
        ordering = ("id",)

    title = models.CharField(max_length=100)
    content = models.TextField()
    created_on = models.DateField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")

    def __str__(self):
        return self.title


class Comment(models.Model):
    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_on = models.DateField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")

    def __str__(self):
        return f"{self.author}, {self.post}, {self.content}"
