from django.urls import path
from django.urls import include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet
from .views import BookList

router = DefaultRouter()
router.register('books', BookViewSet, basename='book')
urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
    path('', include(router.urls)),
]