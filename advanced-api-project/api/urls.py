from django.urls import path
from .views import BookListView
from .views import BookDetailView

urlpatterns = [
    path('books/', BookListView.as_view(), name='book-list'),
    path('book/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
]