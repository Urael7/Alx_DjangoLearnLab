from django.db import models

class Author(models.Model):
    """
    Author model represents a writer who can have multiple books.
    One Author can be linked to many Book instances.
    """
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Book(models.Model):
    """
    Book model represents a published book.
    Each book is linked to a single Author (many-to-one relationship).
    """
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    author = models.ForeignKey(
        Author,
        related_name='books',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title
