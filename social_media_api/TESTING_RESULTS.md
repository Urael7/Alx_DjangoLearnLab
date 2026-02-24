# Testing Results: Likes and Notifications

## Scope

Validated likes and notifications functionality in `social_media_api`.

## Automated Tests Added

- `posts.tests.LikeAndNotificationTests`
  - `test_user_can_like_and_unlike_post`
  - `test_like_creates_notification_for_post_author`
  - `test_comment_creates_notification_for_post_author`
- `notifications.tests.NotificationEndpointTests`
  - `test_notifications_endpoint_returns_unread_first`

## Manual Verification Checklist

- [x] Like endpoint rejects duplicate likes.
- [x] Unlike endpoint rejects unliked state.
- [x] Notification is created when user is followed.
- [x] Notification is created when a post is liked.
- [x] Notification is created when a post is commented on.
- [x] Notifications endpoint returns unread notifications first.

## Expected Outcome

All tests pass and endpoints behave as documented.
