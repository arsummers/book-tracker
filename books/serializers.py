from rest_framework import serializers
from books.models import Author, Book, MediaType

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['name']

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'author']

class MediaTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = MediaType
        fields = ['media_type']