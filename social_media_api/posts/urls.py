from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet
from .views import user_feed
from .views import like_post, unlike_post


router = DefaultRouter()
router.register('posts', PostViewSet)
router.register('comments', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('feed/', user_feed, name='user_feed'),
    path('<int:pk>/like/', like_post, name='like_post'),
    path('<int:pk>/unlike/', unlike_post, name='unlike_post'),
]