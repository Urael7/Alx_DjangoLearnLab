from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import permission_required
from .models import Book
from relationship_app.models import Library

# View for all libraries
@permission_required('bookshelf.can_view', raise_exception=True)
def library_list(request):
    libraries = Library.objects.all()
    return render(request, "bookshelf/library_list.html", {"libraries": libraries})

# View for books in a library
@permission_required('bookshelf.can_view', raise_exception=True)
def library_detail(request, pk):
    library = get_object_or_404(Library, pk=pk)
    books = library.books.all()  # related_name in ForeignKey
    return render(request, "bookshelf/library_detail.html", {"library": library, "books": books})


# View for all books
@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, "bookshelf/book_list.html", {"books": books})
