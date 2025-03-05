from .models import Author, Book, Library, Librarian

def get_books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        return Author.objects.filter(author=author)
    except Author.DoesNotExist:
        return "Author not found"

def get_all_books_in_library(library_name):
    try:
        Library.objects.get(name=library_name)
        return Library.books.all()
    except Library.DoesNotExist:
        return "Library not found"

def get_librarian_for_a_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        return Librarian.objects.get(library=library)
    except (Library.DoesNotExist, Librarian.DoesNotExist):
        return "Library or Librarian not found"