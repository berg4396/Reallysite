from django.db import models
from django.contrib.auth import get_user_model

class Article(models.Model):
    title = models.CharField(default="" , max_length=30)

    text = models.TextField(default="" ,)

    auther = models.CharField(default="" ,max_length=30)

    created_at = models.DateField(auto_now_add=True)

    update_at = models.DateField(auto_now=True)

class Commnet(models.Model):
    comment = models.TextField(default="", max_length=500)

    created_at= models.DateField(auto_now_add=True)

    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    article = models.ForeignKey(Article, on_delete=models.CASCADE)

