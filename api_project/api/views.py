from rest_framework import generics, viewsets
from .models import Book
from .serializers import BookSerializer
from rest_framework import generics, viewsets, permissions



# ListAPIView (from previous task – KEEP IT)
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


# ViewSet for full CRUD operations
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # <-- enforce login
# BookViewSet uses TokenAuthentication and IsAuthenticated permission
# Only users with valid token can list, create, update, or delete books
