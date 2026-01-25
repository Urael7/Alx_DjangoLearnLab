from django.urls import path
from . import views

urlpatterns = [
    path('libraries/', views.library_list, name='library_list'),
    path('libraries/<int:pk>/', views.library_detail, name='library_detail'),
    path('books/', views.book_list, name='book_list'),
]
