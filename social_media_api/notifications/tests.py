from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from posts.models import Post
from .models import Notification


User = get_user_model()


class NotificationEndpointTests(APITestCase):
    def setUp(self):
        self.recipient = User.objects.create_user(username='recipient', password='pass1234')
        self.actor = User.objects.create_user(username='actor', password='pass1234')
        self.post = Post.objects.create(author=self.recipient, title='Post', content='Body')
        content_type = ContentType.objects.get_for_model(self.post)

        self.read_notification = Notification.objects.create(
            recipient=self.recipient,
            actor=self.actor,
            verb='older notification',
            target_content_type=content_type,
            target_object_id=self.post.id,
            is_read=True,
        )
        self.unread_notification = Notification.objects.create(
            recipient=self.recipient,
            actor=self.actor,
            verb='new unread notification',
            target_content_type=content_type,
            target_object_id=self.post.id,
            is_read=False,
        )

    def test_notifications_endpoint_returns_unread_first(self):
        self.client.force_authenticate(user=self.recipient)
        url = reverse('notifications-list')

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        results = response.data.get('results', response.data)
        self.assertGreaterEqual(len(results), 2)
        self.assertEqual(results[0]['id'], self.unread_notification.id)
