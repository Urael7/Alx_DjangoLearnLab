from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import permission_required
from .models import Book
from .forms import BookSearchForm, ExampleForm
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
    form = BookSearchForm(request.GET or None)
    books = Book.objects.all()
    if form.is_valid():
        q = form.cleaned_data.get('q')
        if q:
            # Safe, parameterized ORM query – avoids SQL injection
            books = books.filter(title__icontains=q)
    context = {"books": books, "form": form}
    return render(request, "bookshelf/book_list.html", context)


@permission_required('bookshelf.can_view', raise_exception=True)
def form_example(request):
    # Demonstrates CSRF on POST and safe handling via Django forms
    if request.method == 'POST':
        form = BookSearchForm(request.POST)
        if form.is_valid():
            q = form.cleaned_data.get('q')
            result = Book.objects.filter(title__icontains=q) if q else Book.objects.none()
            return render(request, "bookshelf/form_example.html", {"form": form, "result": ", ".join(b.title for b in result)})
    else:
        form = BookSearchForm()
    return render(request, "bookshelf/form_example.html", {"form": form})
