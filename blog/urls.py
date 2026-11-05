from django.urls import path

from .views import (
    create_user,
    create_category,
    create_post,
    create_comment,
    get_posts,
    generate_post,
    summarize_post_view
)

urlpatterns = [
    path('users/', create_user, name='create_user'),
    path('categories/', create_category, name='create_category'),
    path('posts/', create_post, name='create_post'),
    path('comments/', create_comment, name='create_comment'),

    path('posts/get_post/', get_posts, name='get_posts'),
    path('posts/generate/', generate_post, name='generate_post'),
    path('posts/<int:post_id>/summarize/',summarize_post_view,name='summarize_post'),
]