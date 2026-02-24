from rest_framework import generics, status, viewsets, permissions
from rest_framework.response import Response
from rest_framework.decorators import action, api_view, permission_classes
from django.shortcuts import get_object_or_404
from .serializers import RegisterSerializer, LoginSerializer, UserSerializer
from .models import User as CustomUser

# -----------------------
# Auth & Profile Views
# -----------------------

class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]


class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data, status=status.HTTP_200_OK)


class ProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user

# -----------------------
# User Follow/Unfollow
# -----------------------

class UserViewSet(viewsets.ModelViewSet):
    """
    ALX-compatible UserViewSet with followuser/unfollowuser actions.
    """
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    http_method_names = ['get', 'post', 'patch', 'delete']

    @action(detail=True, methods=['post'], permission_classes=[permissions.IsAuthenticated])
    def followuser(self, request, pk=None):
        user_to_follow = self.get_object()
        if user_to_follow == request.user:
            return Response({"detail": "Cannot follow yourself."}, status=status.HTTP_400_BAD_REQUEST)
        request.user.following.add(user_to_follow)
        return Response({"detail": f"You are now following {user_to_follow.username}."})

    @action(detail=True, methods=['post'], permission_classes=[permissions.IsAuthenticated])
    def unfollowuser(self, request, pk=None):
        user_to_unfollow = self.get_object()
        if user_to_unfollow == request.user:
            return Response({"detail": "Cannot unfollow yourself."}, status=status.HTTP_400_BAD_REQUEST)
        request.user.following.remove(user_to_unfollow)
        return Response({"detail": f"You have unfollowed {user_to_unfollow.username}."})


@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def follow_user(request, user_id):
    user_to_follow = get_object_or_404(CustomUser, id=user_id)
    if user_to_follow == request.user:
        return Response({"detail": "Cannot follow yourself."}, status=status.HTTP_400_BAD_REQUEST)
    request.user.following.add(user_to_follow)
    return Response({"detail": f"You are now following {user_to_follow.username}."}, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def unfollow_user(request, user_id):
    user_to_unfollow = get_object_or_404(CustomUser, id=user_id)
    if user_to_unfollow == request.user:
        return Response({"detail": "Cannot unfollow yourself."}, status=status.HTTP_400_BAD_REQUEST)
    request.user.following.remove(user_to_unfollow)
    return Response({"detail": f"You have unfollowed {user_to_unfollow.username}."}, status=status.HTTP_200_OK)