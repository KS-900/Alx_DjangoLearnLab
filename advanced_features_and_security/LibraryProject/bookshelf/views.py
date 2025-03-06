from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from .models import Book

# Create your views here.
@permission_required('bookshelf.can_create', raise_exception=True)
def create_book(request):
    return "pemission granted"
def book_list(request):
    return Book.objects.all()
@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request):
    return "permission granted"
@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request):
    return "permission granted"