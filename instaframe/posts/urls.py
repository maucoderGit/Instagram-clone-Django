"""Posts urls"""

# Django
from django.urls import path

# Views
from . import views


app_name = 'posts'
urlpatterns = [
    path('', view=views.PostsFeedView.as_view(), name='feed'),
    path('posts/new/', views.CreatePostView.as_view(), name='create'),
    path('posts/<int:pk>/', views.PostDetailView.as_view(), name='detail')
]
