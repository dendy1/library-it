from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('clients/', views.client_list, name='clients'),
    path('client/add/', views.client_add, name='client_add'),
    path('client/<int:pk>/edit/', views.client_edit, name='client_edit'),
    path('client/<int:pk>/delete/', views.client_delete, name='client_delete'),
    path('client/<int:pk>/details/', views.client_details, name='client_details'),
    path('client/<int:pk>/fine/<int:fine>/', views.client_fine, name='client_fine'),
    path('books/', views.book_list, name='books'),
    path('book/add/', views.book_add, name='book_add'),
    path('book/<int:pk>/edit/', views.book_edit, name='book_edit'),
    path('book/<int:pk>/delete/', views.book_delete, name='book_delete'),
    path('extend/<int:pk>/', views.extend, name='client_fine'),
]