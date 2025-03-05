from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import list_books, LibraryDetailView

urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path('login/', auth_views.LoginView.as_view(template_name= 'login.html'), name='login'),
    path('login/', auth_views.LogoutView.as_view(template_name= 'logout.html'), name='logout'),
    path('register/', views.register, name='register'),
    path('admin/', views.admin_view, name='admin_view'),
    path('librarian/', views.librarian_view, name='librarian_view'),
    path('member/', views.member_view, name='member_view'),
    path('add_book/', views.add_book, name='add_book'),
    path('edit_book/', views.change_book, name='edit_book'),
    path('delete/', views.delete_book, name='delete_book'),
]