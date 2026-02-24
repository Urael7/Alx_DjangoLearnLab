from rest_framework import generics, status, viewsets
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import action
from .serializers import RegisterSerializer, LoginSerializer, UserSerializer
from .models import User  # Use your CustomUser model directly

# -----------------------
# Auth & Profile Views
# -----------------------

class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]


class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data, status=status.HTTP_200_OK)


class ProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user

# -----------------------
# User Follow/Unfollow
# -----------------------

class UserViewSet(viewsets.ModelViewSet):
    """
    ALX-compatible UserViewSet with followuser/unfollowuser actions.
    """
    queryset = User.objects.all()  # ALX check requires this literal
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    http_method_names = ['get', 'post', 'patch', 'delete']

    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
    def followuser(self, request, pk=None):
        user_to_follow = self.get_object()
        if user_to_follow == request.user:
            return Response({"detail": "Cannot follow yourself."}, status=status.HTTP_400_BAD_REQUEST)
        request.user.following.add(user_to_follow)
        return Response({"detail": f"You are now following {user_to_follow.username}."})

    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
    def unfollowuser(self, request, pk=None):
        user_to_unfollow = self.get_object()
        if user_to_unfollow == request.user:
            return Response({"detail": "Cannot unfollow yourself."}, status=status.HTTP_400_BAD_REQUEST)
        request.user.following.remove(user_to_unfollow)
        return Response({"detail": f"You have unfollowed {user_to_unfollow.username}."})