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
