from django.shortcuts import render, redirect 
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from .models import Book, Library
from django.views.generic import DetailView
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import permission_required
from django.contrib.auth import login

relationship_app/list_books.html, Book.objects.all()
def list_books(request):
    books =  Book.objects.all()
    response_text = "\n".join([f"{book.title} by {book.author.name}" for book in books])
    return HttpResponse(f"<pre>{response_text} </pre>")

class LibraryDetailView(DetailView):
    def get(self, request, pk):
        try:
            library = Library.objects.get(pk = pk)
            books = library.books.all()
            book_list = "\n".join([f"{book.title} by {book.author.name}" for book in books])
            return HttpResponse(f"Library: {library.name}\n{book_list}", content_type="text/plain")
        except Library.DoesNotExist:
            return HttpResponse("Library not found", status=404)

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def is_admin(user):
    return user.userprofile.role == 'Admin'
@user_passes_test(is_admin)
def admin_view(request):
    return HttpResponse('welcome, Admin')

def is_librarian(user):
    return user.userprofile.role == 'Librarian'
@user_passes_test(is_librarian)
def librarian_view(request):
    return HttpResponse("Welcome, Librarian")

def is_member(user):
    return user.userprofile.role == 'Member'
@user_passes_test(is_member)
def member_view(request):
    return HttpResponse("Welcome, Member")

@permission_required('relationship_app.can_add_book')
def add_book(request):

    pass

@permission_required('relationship_app.can_change_book')
def change_book(request):

    pass

@permission_required('relationship_app.can_delete_book')
def delete_book(request):

    pass