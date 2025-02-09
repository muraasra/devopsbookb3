from rest_framework.test import APIClient
from rest_framework import status
from .models import Author, Book
from django.test import TestCase

class ViewSetTests(TestCase):
    def setUp(self):
        # Create sample data for testing
        self.client = APIClient()
        self.author = Author.objects.create(
            name="J.K. Rowling",
            birth_date="1965-07-31",
            nationality="British"
        )
        self.book = Book.objects.create(
            title="Harry Potter and the Philosopher's Stone",
            author=self.author,
            publication_date="1997-06-26"
        )

    def test_list_authors(self):
        """Test that authors can be listed."""
        response = self.client.get('/api/author/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_create_author(self):
        """Test that an author can be created."""
        data = {
            "name": "George Orwell",
            "birth_date": "1903-06-25",
            "nationality": "British"
        }
        response = self.client.post('/api/author/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Author.objects.count(), 2)

    # def test_list_books(self):
    #     """Test that books can be listed."""
    #     response = self.client.get('/api/books/')
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertEqual(len(response.data), 1)

    # def test_create_book(self):
    #     """Test that a book can be created."""
    #     data = {
    #         "title": "1984",
    #         "author": self.author.id,
    #         "publication_date": "1949-06-08"
    #     }
    #     response = self.client.post('/api/books/', data, format='json')
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    #     self.assertEqual(Book.objects.count(), 2)
