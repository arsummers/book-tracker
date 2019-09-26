from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=255, default='no one')

    def __str__(self):
        return f'Name: {self.name}'

class Book(models.Model):
    title = models.CharField(max_length=255, default='nothing')
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return f'Title: {self.title} \n Author: {self.author}'
