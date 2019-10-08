from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100, default='unknown')

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

class Book(models.Model):
    MEDIA_TYPE = (
        ('ZINE', 'zine'),
        ('BOOK', 'book'),
        ('VIDEO', 'video'),
        ('COMIC', 'comic'),
    )

    title = models.CharField(max_length=255, default='nothing')
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    media_type = models.CharField(max_length=1, choices=MEDIA_TYPE, default='None')


    class Meta:
        ordering = ('title',)
    def __str__(self):
        return f'Title: {self.title} \n Author: {self.author} \n Type: {self.media_type}' 