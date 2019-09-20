from django.shortcuts import render
from models import Books
from rest_framework import viewsets
from serializers import BooksSerializer

class BooksViewSet(viewsets.ModelViewSet):
    serializer_class = BooksSerializer
