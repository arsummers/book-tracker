from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100, default='unknown')

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

class MediaType(models.Model):
    media_type = models.CharField(max_length=50, default='unknown')

class Book(models.Model):
    title = models.CharField(max_length=255, default='nothing')
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    media_type = models.ForeignKey(MediaType, on_delete=models.CASCADE)


    class Meta:
        ordering = ('title',)
    def __str__(self):
        return f'Title: {self.title} \n Author: {self.author} \n Type: {self.media_type}' 