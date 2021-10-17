from django.db import models

class Article(models.Model):
    title = models.CharField(default="" , max_length=30)

    text = models.TextField(default="" ,)

    auther = models.CharField(default="" ,max_length=30)

    created_at = models.DateField(auto_now_add=True)

    update_at = models.DateField(auto_now=True)
