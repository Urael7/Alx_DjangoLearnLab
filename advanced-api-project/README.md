# Advanced API Project

## Overview
This project demonstrates the use of Django REST Framework generic views
to implement CRUD operations for a Book model.

## API Endpoints

- GET /api/books/  
  Retrieve all books (public access)

- GET /api/books/<id>/  
  Retrieve a single book by ID (public access)

- POST /api/books/create/  
  Create a new book (authenticated users only)

- PUT /api/books/<id>/update/  
  Update an existing book (authenticated users only)

- DELETE /api/books/<id>/delete/  
  Delete a book (authenticated users only)

## Permissions
- Read operations are publicly accessible
- Write operations require authentication

## Technologies
- Django
- Django REST Framework
- SQLite

## Filtering, Searching, and Ordering

### Filtering
Books can be filtered using query parameters:
- /api/books/?title=Python
- /api/books/?publication_year=2023
- /api/books/?author=1

### Searching
Text search is supported on book title and author name:
- /api/books/?search=django

### Ordering
Results can be ordered by title or publication year:
- /api/books/?ordering=title
- /api/books/?ordering=-publication_year