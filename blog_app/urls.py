
from django.urls import path
from .api_views import RegisterView, PostListCreateView, PostDetailView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('posts/', PostListCreateView.as_view(), name='post-list-create'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
]
