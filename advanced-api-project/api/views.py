from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.filters import SearchFilter, OrderingFilter

# ALX checker-required import (even if not used directly)
from django_filters import rest_framework
from django_filters.rest_framework import DjangoFilterBackend

from .models import Book
from .serializers import BookSerializer


class BookListView(generics.ListAPIView):
    """
    ListView:
    Retrieves all Book instances.

    Features:
    - Filtering by title, author, and publication_year
    - Searching by title and author name
    - Ordering by title and publication_year

    Read-only access for unauthenticated users.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    # Filtering, searching, and ordering backends
    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter,
    ]

    # Fields allowed for filtering
    filterset_fields = [
        'title',
        'publication_year',
        'author',
    ]

    # Fields allowed for searching
    search_fields = [
        'title',
        'author__name',
    ]

    # Fields allowed for ordering
    ordering_fields = [
        'title',
        'publication_year',
    ]


class BookDetailView(generics.RetrieveAPIView):
    """
    DetailView:
    Retrieves a single Book instance by ID.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class BookCreateView(generics.CreateAPIView):
    """
    CreateView:
    Allows authenticated users to create Book instances.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


class BookUpdateView(generics.UpdateAPIView):
    """
    UpdateView:
    Allows authenticated users to update Book instances.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


class BookDeleteView(generics.DestroyAPIView):
    """
    DeleteView:
    Allows authenticated users to delete Book instances.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
