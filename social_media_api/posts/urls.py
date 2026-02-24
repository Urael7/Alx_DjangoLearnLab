from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet, FeedViewSet, like_post, unlike_post

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')
router.register(r'comments', CommentViewSet, basename='comment')

urlpatterns = [
	path('feed/', FeedViewSet.as_view({'get': 'list'}), name='feed'),
	path('posts/<int:pk>/like/', like_post, name='post-like'),
	path('posts/<int:pk>/unlike/', unlike_post, name='post-unlike'),
]

urlpatterns += router.urls