from django.http import HttpResponse
from django.views.generic import DetailView
from relationship_app.models import Book, Library

def list_books(request):
    books = Book.objects.all()
    return HttpResponse(
        "\n".join([f"{book.title} by {book.author.name}" for book in books])
    )

class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"
