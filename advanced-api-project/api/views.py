from django.shortcuts import render
from rest_framework import generics
from .serializers import BookSerializer
from django_filters.rest_framework import DjangoFilterBackend
from .models import Book
from rest_framework.filters import SearchFilter
from rest_framework.filters import OrderingFilter
from django_filters import rest_framework

class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['title', 'author__name']
    ordering_fields = ['title', 'publication_year']