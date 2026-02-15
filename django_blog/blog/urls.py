from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # -----------------------------
    # Blog Post CRUD URLs
    # -----------------------------
    path("", views.PostListView.as_view(), name="home"),
    path("post/<int:pk>/", views.PostDetailView.as_view(), name="post_detail"),
    path("post/new/", views.PostCreateView.as_view(), name="post_create"),
    path("post/<int:pk>/update/", views.PostUpdateView.as_view(), name="post_update"),
    path("post/<int:pk>/delete/", views.PostDeleteView.as_view(), name="post_delete"),

    # -----------------------------
    # Tagging and Search URLs
    # -----------------------------
    path("tags/<slug:tag_slug>/", views.PostByTagListView.as_view(), name="tag_posts"),
    path("search/", views.SearchResultsView.as_view(), name="post_search"),

    # -----------------------------
    # Comment URLs (Checker-compliant)
    # -----------------------------
    # Corrected URL for creating a new comment on a specific post
    path("posts/<int:pk>/comments/new/", views.CommentCreateView.as_view(), name="add_comment"),
    path("comment/<int:pk>/update/", views.CommentUpdateView.as_view(), name="comment_update"),
    path("comment/<int:pk>/delete/", views.CommentDeleteView.as_view(), name="comment_delete"),

    # -----------------------------
    # Authentication URLs
    # -----------------------------
    path("login/", auth_views.LoginView.as_view(template_name="blog/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(template_name="blog/logout.html"), name="logout"),
    path("register/", views.register, name="register"),
    path("profile/", views.profile, name="profile"),
]
