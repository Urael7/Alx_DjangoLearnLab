from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication

from django_filters.rest_framework import DjangoFilterBackend

from .models import Book
from .serializers import BookSerializer


class CsrfExemptSessionAuthentication(SessionAuthentication):
    """
    Custom SessionAuthentication that disables CSRF checks.
    This avoids CSRF-related 403 errors during API testing.
    """
    def enforce_csrf(self, request):
        return


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

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]

    filterset_fields = [
        'title',
        'publication_year',
        'author',
    ]

    search_fields = [
        'title',
        'author__name',
    ]

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
    Allows authenticated users to create a new Book.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # Use TokenAuthentication first so unauthenticated requests return 401 (ALX expected)
    authentication_classes = [
        TokenAuthentication,
        BasicAuthentication,
        CsrfExemptSessionAuthentication,
    ]

    # Only one permission class is needed
    permission_classes = [IsAuthenticated]


class BookUpdateView(generics.UpdateAPIView):
    """
    UpdateView:
    Allows authenticated users to update Book instances.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    authentication_classes = [
        TokenAuthentication,
        BasicAuthentication,
        CsrfExemptSessionAuthentication,
    ]

    permission_classes = [IsAuthenticated]


class BookDeleteView(generics.DestroyAPIView):
    """
    DeleteView:
    Allows authenticated users to delete Book instances.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    authentication_classes = [
        TokenAuthentication,
        BasicAuthentication,
        CsrfExemptSessionAuthentication,
    ]

    permission_classes = [IsAuthenticated]
