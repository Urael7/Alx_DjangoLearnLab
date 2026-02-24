from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import RegisterView, LoginView, ProfileView, UserViewSet, follow_user, unfollow_user

# Create router and register UserViewSet
router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')

# URL patterns
urlpatterns = [
    # Auth endpoints
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('follow/<int:user_id>/', follow_user, name='follow-user'),
    path('unfollow/<int:user_id>/', unfollow_user, name='unfollow-user'),
]

# Include router URLs for UserViewSet
urlpatterns += router.urls