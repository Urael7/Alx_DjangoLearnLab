from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient

from api.models import Author, Book


class BookAPITestCase(APITestCase):
    """
    Test suite for Book API endpoints.
    Covers CRUD operations, permissions,
    filtering, searching, and ordering.
    """

    def setUp(self):
        """
        Set up test data and users.
        This runs before every test.
        """
        # Create user for authenticated actions
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )

        # Create author
        self.author = Author.objects.create(name="Test Author")

        # Create books
        self.book1 = Book.objects.create(
            title="Django Basics",
            publication_year=2020,
            author=self.author
        )

        self.book2 = Book.objects.create(
            title="Advanced Django",
            publication_year=2022,
            author=self.author
        )

        # API endpoints
        self.list_url = "/api/books/"
        self.create_url = "/api/books/create/"
        self.update_url = f"/api/books/update/{self.book1.id}/"
        self.delete_url = f"/api/books/delete/{self.book1.id}/"

    # -------------------------
    # READ OPERATIONS
    # -------------------------

    def test_get_all_books(self):
        """
        Ensure unauthenticated users can retrieve all books.
        """
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_get_single_book(self):
        """
        Ensure a single book can be retrieved by ID.
        """
        response = self.client.get(f"/api/books/{self.book1.id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], self.book1.title)

    # -------------------------
    # CREATE
    # -------------------------

    def test_create_book_requires_authentication(self):
        """
        Ensure unauthenticated users cannot create a book.
        """
        data = {
            "title": "Unauthorized Book",
            "publication_year": 2021,
            "author": self.author.id
        }
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_book_authenticated(self):
        """
        Ensure authenticated users can create a book.
        """
        self.client.login(username="testuser", password="testpassword")

        data = {
            "title": "New Django Book",
            "publication_year": 2021,
            "author": self.author.id
        }

        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)

    # -------------------------
    # UPDATE
    # -------------------------

    def test_update_book_authenticated(self):
        """
        Ensure authenticated users can update a book.
        """
        self.client.login(username="testuser", password="testpassword")

        data = {
            "title": "Updated Django Title",
            "publication_year": 2020,
            "author": self.author.id
        }

        response = self.client.put(self.update_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Updated Django Title")

    # -------------------------
    # DELETE
    # -------------------------

    def test_delete_book_authenticated(self):
        """
        Ensure authenticated users can delete a book.
        """
        self.client.login(username="testuser", password="testpassword")

        response = self.client.delete(self.delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    # -------------------------
    # FILTERING
    # -------------------------

    def test_filter_books_by_publication_year(self):
        """
        Ensure books can be filtered by publication year.
        """
        response = self.client.get(f"{self.list_url}?publication_year=2022")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    # -------------------------
    # SEARCHING
    # -------------------------

    def test_search_books_by_title(self):
        """
        Ensure books can be searched by title.
        """
        response = self.client.get(f"{self.list_url}?search=Advanced")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    # -------------------------
    # ORDERING
    # -------------------------

    def test_order_books_by_title(self):
        """
        Ensure books can be ordered by title.
        """
        response = self.client.get(f"{self.list_url}?ordering=title")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]["title"], "Advanced Django")
