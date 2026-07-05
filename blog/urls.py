from django.urls import path, include

from blog.views import (
    PostListView,
    PostDetailView,
    UserDetailView,
)

urlpatterns = [
    path("post/", PostListView.as_view(), name="index"),
    path("post/<int:pk>", PostDetailView.as_view(), name="post-detail"),
    path("user/<int:pk>", UserDetailView.as_view(), name="user-detail"),
]

app_name = "blog"
