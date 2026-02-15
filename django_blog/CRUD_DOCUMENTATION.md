# Blog Post Management Features (CRUD)

## Implemented Features
This Django blog supports full CRUD operations using Django Class-Based Views:

- ListView: Display all posts
- DetailView: Display single post
- CreateView: Create new post (authenticated users only)
- UpdateView: Edit post (only author)
- DeleteView: Delete post (only author)

## URLs
- /posts/ → list all posts
- /posts/new/ → create post
- /posts/<pk>/ → view post detail
- /posts/<pk>/edit/ → edit post
- /posts/<pk>/delete/ → delete post

## Permissions
- Anyone can view posts
- Only logged-in users can create posts
- Only the author of the post can edit/delete posts

## How to Test
1. Run server:
   python manage.py runserver

2. Open:
   http://127.0.0.1:8000/posts/

3. Create new post:
   http://127.0.0.1:8000/posts/new/

4. Try editing/deleting as another user to confirm permission works.
