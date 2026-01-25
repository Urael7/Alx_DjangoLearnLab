from django.shortcuts import render, get_object_or_404
from .models import Book

# View for all libraries
def library_list(request):
    libraries = Library.objects.all()
    return render(request, "bookshelf/library_list.html", {"libraries": libraries})

# View for books in a library
def library_detail(request, pk):
    library = get_object_or_404(Library, pk=pk)
    books = library.books.all()  # related_name in ForeignKey
    return render(request, "bookshelf/library_detail.html", {"library": library, "books": books})
