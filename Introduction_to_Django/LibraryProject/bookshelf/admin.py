from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    search_fields = ('title', 'author')
    list_filter =('publication_year',)
if not admin.site.is_registered(Book, BookAdmin):
    admin.site.register(Book, BookAdmin)