from rest_framework import serializers
from .models import Author
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model =Book
        fields = '__all__'

class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)
    class Meta:
        model = Author 
        fields = ['id', 'name', 'books']

    def validate_publication_year(self, value):
        from datetime import datetime
        if value > datetime.now().year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value 