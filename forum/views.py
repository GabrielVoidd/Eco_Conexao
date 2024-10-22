from rest_framework import status
from .models import Post, Comment, Topic, SubTopic
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView


class TopicCreateView(CreateView):
    model = Topic
    fields = ['title', 'description']
    template_name = 'templates/topic_form.html'
    success_url = reverse_lazy('topic-list')


class TopicListView(ListView):
    model = Topic
    template_name = 'templates/topic_list.html'
    context_object_name = 'topics'


class TopicDetailView(DetailView):
    model = Topic
    template_name = 'templates/topic_detail.html'
    context_object_name = 'topic'


class SubTopicCreateView(CreateView):
    model = SubTopic
    fields = ['title', 'description', 'topic']
    template_name = 'templates/subtopic_form.html'
    success_url = reverse_lazy('subtopic-list')


class SubTopicListView(ListView):
    model = SubTopic
    template_name = 'templates/subtopic_list.html'
    context_object_name = 'subtopics'


class SubTopicDetailView(DetailView):
    model = SubTopic
    template_name = 'templates/subtopic_detail.html'
    context_object_name = 'subtopic'


class SubTopicUpdateView(UpdateView):
    model = SubTopic
    fields = ['title', 'description']
    template_name = 'templates/subtopic_form.html'
    success_url = reverse_lazy('subtopic-list')


class SubTopicDeleteView(DeleteView):
    model = SubTopic
    template_name = 'templates/subtopic_confirm_delete.html'
    success_url = reverse_lazy('subtopic-list')


class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'content', 'author', 'subtopic']
    template_name = 'templates/post_form.html'
    success_url = reverse_lazy('post-list')


class PostListView(ListView):
    model = Post
    template_name = 'templates/post_list.html'
    context_object_name = 'posts'


class PostDetailView(DetailView):
    model = Post
    template_name = 'templates/post_detail.html'
    context_object_name = 'post'


class PostUpdateView(UpdateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'templates/post_form.html'
    success_url = reverse_lazy('post-list')


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'templates/post_confirm_delete.html'
    success_url = reverse_lazy('post-list')


class CommentCreateView(CreateView):
    model = Comment
    fields = ['content', 'author', 'post']
    template_name = 'templates/comment_form.html'
    success_url = reverse_lazy('post-list')  # Retorna para a lista de posts


class CommentUpdateView(UpdateView):
    model = Comment
    fields = ['content']
    template_name = 'templates/comment_form.html'
    success_url = reverse_lazy('post-list')


class CommentDeleteView(DeleteView):
    model = Comment
    template_name = 'templates/comment_confirm_delete.html'
    success_url = reverse_lazy('post-list')


class LogoutView(APIView):
    """"Com APIView eu posso definir respostas HTTP"""
    permission_classes = [IsAuthenticated]

    def post(self, request):
        """"Exige que o usuário esteja autenticado"""
        permission_classes = [IsAuthenticated]

        def post(self, request):
            try:
                # Verifica e deleta o token do usuário autenticado
                request.user.auth_token.delete()
                return Response(status=status.HTTP_204_NO_CONTENT )
            except (AttributeError, Token.DoesNotExist):
                return Response({"error": "Token não encontrado ou já foi invalidado."},
                                  status=status.HTTP_400_BAD_REQUEST )


def home(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'home.html', {'posts': posts})


def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'post_detail.html', {'post': post})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


class CustomLoginView(LoginView):
    template_name = 'login.html'
