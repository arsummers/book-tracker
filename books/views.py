from rest_framework import generics
from books.models import Author, Book, MediaType
from books.serializers import AuthorSerializer, BookSerializer, MediaTypeSerializer

class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDetail(generics.RetrieveUpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class AuthorList(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class AuthorDetail(generics.RetrieveUpdateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class MediaTypeList(generics.ListCreateAPIView):
    queryset = MediaType.objects.all()
    serializer_class = MediaTypeSerializer

class MediaTypeDetail(generics.RetrieveUpdateAPIView):
    queryset = MediaType.objects.all()
    serializer_class = MediaTypeSerializer