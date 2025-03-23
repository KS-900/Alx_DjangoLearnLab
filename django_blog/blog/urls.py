from django.urls import path
from .views import register, user_login, user_logout, home, profile
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView


urlpatterns = [
    path('profile/', profile, name='profile'),
    path('home/', home, name='home'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('', PostListView.as_view(), name='post-list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/edit/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
]