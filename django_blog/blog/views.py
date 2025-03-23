from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import get_object_or_404
from django.http import JsonResponse, HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .models import Post

def home(request):
    return render(request, 'blog/base.html')

def profile(request):
    return render(request, 'blog/profile.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'blog/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'blog/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('home')

class PostListView(ListView):
    model = Post

    def render_to_response(self, context, **response_kwargs):
        posts = list(self.get_queryset().values('id', 'title', 'content', 'published_date', 'author_id'))
        return JsonResponse({'posts': posts}, safe=False)
    
class PostDetailView(DetailView):
    model = Post

    def render_to_response(self, context, **response_kwargs):
        post = {
            'id': self.object.id,
            'title': self.object.title,
            'content': self.object.content,
            'published_date': self.object.published_date,
            'author_id': self.object.author_id
        }
        return JsonResponse({'post': post}, safe=False)
    
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        post = form.save()
        return JsonResponse({'message': 'Post created successfully!', 'post_id': post.id}, status=201)

    def form_invalid(self, form):
        return JsonResponse({'errors': form.errors}, status=400)
    
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        post = form.save()
        return JsonResponse({'message': 'Post updated successfully!', 'post_id': post.id}, status=200)

    def form_invalid(self, form):
        return JsonResponse({'errors': form.errors}, status=400)

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('post-list')

    def delete(self, request, *args, **kwargs):
        post = self.get_object()
        post.delete()
        return JsonResponse({'message': 'Post deleted successfully!'}, status=200)

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

