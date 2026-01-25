from django.shortcuts import render
from django.views.generic import ListView
from .models import Book, Library
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {
        'books': books
    })
class LibraryDetailView(ListView):
    model = Book
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'books'

    def get_queryset(self):
        self.library = Library.objects.get(pk=self.kwargs['pk'])
        return Book.objects.filter(library=self.library)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['library'] = self.library
        return context
