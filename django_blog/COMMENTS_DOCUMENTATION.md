# Comment Functionality Documentation

## Features Implemented
- Users can view comments under each post.
- Authenticated users can add new comments.
- Only the comment author can edit or delete their comment.

## Comment Model Fields
- post (ForeignKey to Post)
- author (ForeignKey to User)
- content (TextField)
- created_at (DateTimeField)
- updated_at (DateTimeField)

## URLs
- Add comment: /post/<pk>/comment/new/
- Update comment: /comment/<pk>/update/
- Delete comment: /comment/<pk>/delete/

## Permissions
- Anyone can read comments.
- Only logged-in users can create comments.
- Only comment owner can update/delete their comment.
