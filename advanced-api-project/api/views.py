from django.shortcuts import render
from rest_framework import generics
from .serializers import BookSerializer
from django_filters.rest_framework import DjangoFilterBackend
from .models import Book
from rest_framework import filters
from rest_framework.filters import SearchFilter
from rest_framework.filters import OrderingFilter
from django_filters import rest_framework
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class BookListView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'author__name']
    ordering_fields = ['title', 'publication_year']

    def perform_create(self, serializer):
        serializer.save()

class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]