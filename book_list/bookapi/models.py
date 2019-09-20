from django.db import models

# Create your models here.
class Books(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)

    def __str__(self):
        return f'Title: {self.title} \n Author: {self.author} \n Genre: {self.genre}'