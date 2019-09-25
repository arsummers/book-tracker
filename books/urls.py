from django.urls import path
from books import views

urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.book_list),
    path('books/<int:pk>/', views.book_detail),
]