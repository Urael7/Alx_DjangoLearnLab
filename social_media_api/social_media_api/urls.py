from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),  # browsable API login
    path('api/', include('posts.urls')),               # posts, comments, feed
    path('api/', include('accounts.urls')),            # users, follow/unfollow, auth
    path('api/', include('notifications.urls')),       # notifications
]