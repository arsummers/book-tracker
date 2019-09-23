from django.shortcuts import render
from django.http import HttpResponse
from books.models import Author, Book
from books.serializers import AuthorSerializer, BookSerializer

def index(request):
    return HttpResponse('this a homepage?')

