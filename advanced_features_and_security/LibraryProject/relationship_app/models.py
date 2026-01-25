from django.db import models


# =========================
# LIBRARY MODEL
# =========================
class Library(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


# =========================
# BOOK MODEL
# =========================
class Book(models.Model):
    title = models.CharField(max_length=255)
    library = models.ForeignKey(
        Library,
        on_delete=models.CASCADE,
        related_name="books"
    )

    def __str__(self):
        return self.title