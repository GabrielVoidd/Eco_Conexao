from django.urls import path
from .views import (PostListView, PostCreateView, PostDetailView, PostUpdateView, PostDeleteView, CommentCreateView,
                    CommentDeleteView, CommentUpdateView, TopicCreateView, TopicListView, TopicDetailView,
                    SubTopicCreateView, SubTopicListView, SubTopicDeleteView, SubTopicDetailView, SubTopicUpdateView)
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('home/', views.home, name='home'),
    path('posts/', PostListView.as_view(), name='post-list'),
    path('posts/new/', PostCreateView.as_view(), name='post-create'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('posts/<int:pk>/edit/', PostUpdateView.as_view(), name='post-edit'),
    path('posts/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('register/', views.register, name='register'),
    path('login/', views.CustomLoginView.as_view(next_page='home'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('topics/', TopicListView.as_view(), name='topic-list'),
    path('topics/<int:pk>/', TopicDetailView.as_view(), name='topic-detail'),
    path('topics/new/', TopicCreateView.as_view(), name='topic-create'),
    path('comments/new/', CommentCreateView.as_view(), name='comment-create'),
    path('comments/<int:pk>/edit/', CommentUpdateView.as_view(), name='comment-edit'),
    path('comments/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),
    path('subtopics/', SubTopicListView.as_view(), name='subtopic-list'),
    path('subtopics/new/', SubTopicCreateView.as_view(), name='subtopic-create'),
    path('subtopics/<int:pk>/', SubTopicDetailView.as_view(), name='subtopic-detail'),
    path('subtopics/<int:pk>/edit/', SubTopicUpdateView.as_view(), name='subtopic-edit'),
    path('subtopics/<int:pk>/delete/', SubTopicDeleteView.as_view(), name='subtopic-delete'),
]
