from django.db import models

# Create your models here. And am currently doing that.
class Article(models.Model):
    title: models.CharField(max_length=200)
    body: models.TextField()
    likes: models.IntegerField()
    pub_date: models.DateTimeField("Published Date")

    def __str__(self):
        return self.title