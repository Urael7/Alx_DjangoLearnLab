>>> from bookshelf.models import Book
>>> book = Book(title="1984", author="George Orwell", publication_year=1949)
>>> book.save()

>>> Book.objects.all()
<QuerySet [<Book: 1984>]>

>>> book.title = "Nineteen Eighty-Four"
>>> book.save()
>>> Book.objects.all()
<QuerySet [<Book: Nineteen Eighty-Four>]>

>>> book.delete()
(1, {'bookshelf.Book': 1})
>>> Book.objects.all()
<QuerySet []>
