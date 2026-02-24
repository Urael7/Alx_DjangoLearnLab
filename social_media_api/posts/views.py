from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from .permissions import IsOwnerOrReadOnly

# -----------------------
# Post & Comment ViewSets
# -----------------------

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['title', 'content']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by('-created_at')
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


# -----------------------
# Feed ViewSet
# -----------------------

class FeedViewSet(viewsets.ViewSet):
    """
    Returns posts from users the current user follows.
    """
    permission_classes = [IsAuthenticated]

    def list(self, request):
        user = request.user
        feed_posts = Post.objects.filter(author__in=user.following.all()).order_by('-created_at')
        serializer = PostSerializer(feed_posts, many=True)
        return Response(serializer.data)