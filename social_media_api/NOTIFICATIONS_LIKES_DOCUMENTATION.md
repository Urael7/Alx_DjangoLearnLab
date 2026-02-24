# Likes and Notifications API Documentation

## Overview

This feature adds post likes and user notifications to improve engagement.

- Users can like and unlike posts.
- Notifications are generated for:
  - New followers
  - Likes on your posts
  - Comments on your posts
- Users can fetch their notifications with unread notifications returned first.

## Endpoints

### 1. Like a Post

- **URL:** `/api/posts/<int:pk>/like/`
- **Method:** `POST`
- **Auth:** Required

**Success Response (201):**

```json
{
  "detail": "Post liked successfully."
}
```

**Already liked (400):**

```json
{
  "detail": "Post already liked."
}
```

### 2. Unlike a Post

- **URL:** `/api/posts/<int:pk>/unlike/`
- **Method:** `POST`
- **Auth:** Required

**Success Response (200):**

```json
{
  "detail": "Post unliked successfully."
}
```

**Not liked yet (400):**

```json
{
  "detail": "Post is not liked yet."
}
```

### 3. Follow User

- **URL:** `/api/follow/<int:user_id>/`
- **Method:** `POST`
- **Auth:** Required

### 4. Unfollow User

- **URL:** `/api/unfollow/<int:user_id>/`
- **Method:** `POST`
- **Auth:** Required

### 5. Fetch Notifications

- **URL:** `/api/notifications/`
- **Method:** `GET`
- **Auth:** Required

**Success Response (200):**

```json
[
  {
    "id": 5,
    "recipient": 2,
    "actor": 1,
    "actor_username": "john",
    "verb": "liked your post",
    "target_content_type": 9,
    "target_object_id": 14,
    "is_read": false,
    "timestamp": "2026-02-24T18:22:00Z"
  }
]
```

## Notification Rules

- Follow notification: created when a user follows another user.
- Like notification: created when someone likes your post.
- Comment notification: created when someone comments on your post.
- Self actions do not create notifications.

## Testing Procedure

1. Create users and posts.
2. Authenticate as another user.
3. Like/unlike posts and verify response codes.
4. Add comments and verify notification creation.
5. Fetch `/api/notifications/` and verify unread notifications appear first.
