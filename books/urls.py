from django.urls import path
from books import views

urlpatterns = [
    path('books/', views.BookList.as_view()),
    path('books/<int:pk>/', views.BookDetail.as_view()),
    path('authors/', views.AuthorList.as_view()),
    path('authors/<int:pk>/', views.AuthorDetail.as_view()),
    path('mediatypes/', views.MediaTypeList.as_view()),
    path('mediatypes/<int:pk>/', views.MediaTypeDetail.as_view())
]
