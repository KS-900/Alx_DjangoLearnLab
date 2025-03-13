from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Book

class BookAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')
        self.book = Book.objects.create(title="Test Book", publication_year=2023, author=self.user)
    
    def test_list_books(self):
        response = self.client.get("/books/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreater(len(response.data), 0)

    def test_create_book(self):
        data = {"title": "New Book", "publication_year": 2024, "author": self.user.id}
        response = self.client.post("/books/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)

    def test_get_single_book(self):
        response = self.client.get(f"/books/{self.book.id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Test Book")

    def test_update_book(self):
        data = {"title": "Updated Book Title", "publication_year": 2022, "author": self.user.id}
        response = self.client.put(f"/books/{self.book.id}/", data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, "Updated Book Title")

    def test_delete_book(self):
        response = self.client.delete(f"/books/{self.book.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

    def test_permission_required(self):
        self.client.logout()
        data = {"title": "Unauthorized Book", "publication_year": 2024, "author": self.user.id}
        response = self.client.post("/books/", data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)