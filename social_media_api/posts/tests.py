from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from notifications.models import Notification
from posts.models import Post, Like


User = get_user_model()


class LikeAndNotificationTests(APITestCase):
	def setUp(self):
		self.author = User.objects.create_user(username='author', password='pass1234')
		self.user = User.objects.create_user(username='user1', password='pass1234')
		self.post = Post.objects.create(author=self.author, title='Hello', content='World')

	def test_user_can_like_and_unlike_post(self):
		self.client.force_authenticate(user=self.user)

		like_url = reverse('post-like', kwargs={'pk': self.post.id})
		unlike_url = reverse('post-unlike', kwargs={'pk': self.post.id})

		like_response = self.client.post(like_url)
		self.assertEqual(like_response.status_code, status.HTTP_201_CREATED)
		self.assertTrue(Like.objects.filter(post=self.post, user=self.user).exists())

		duplicate_like = self.client.post(like_url)
		self.assertEqual(duplicate_like.status_code, status.HTTP_400_BAD_REQUEST)

		unlike_response = self.client.post(unlike_url)
		self.assertEqual(unlike_response.status_code, status.HTTP_200_OK)
		self.assertFalse(Like.objects.filter(post=self.post, user=self.user).exists())

	def test_like_creates_notification_for_post_author(self):
		self.client.force_authenticate(user=self.user)
		like_url = reverse('post-like', kwargs={'pk': self.post.id})

		response = self.client.post(like_url)
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)

		self.assertTrue(
			Notification.objects.filter(
				recipient=self.author,
				actor=self.user,
				verb='liked your post',
			).exists()
		)

	def test_comment_creates_notification_for_post_author(self):
		self.client.force_authenticate(user=self.user)
		comment_url = reverse('comment-list')

		response = self.client.post(comment_url, {'post': self.post.id, 'content': 'Nice post'}, format='json')
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)

		self.assertTrue(
			Notification.objects.filter(
				recipient=self.author,
				actor=self.user,
				verb='commented on your post',
			).exists()
		)
