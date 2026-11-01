from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import (
    PostViewSet,
    UserViewSet,
    CategoryViewSet,
    CommentViewSet,
    get_posts,
)

router = DefaultRouter()

router.register('users', UserViewSet)
router.register('categories', CategoryViewSet)
router.register('posts', PostViewSet)
router.register('comments', CommentViewSet)

urlpatterns = [
    path('posts/get_post/', get_posts, name='get_post'),
]

urlpatterns += router.urls