from django.contrib import admin
from .models import Post, User, Comment, Category
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title_id', 'title', 'author')
    list_filter = ('title_id', 'title', 'author')
    search_fields = ('title_id', 'title', 'author')
    ordering = ('title_id', 'title', 'author')


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'created_at')
    search_fields = ('username', 'email')
    list_filter = ('first_name', 'last_name', 'created_at')
    ordering = ('-created_at',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'author', 'content', 'created_at')
    search_fields = ('post__title', 'author__username', 'content')
    list_filter = ('created_at', 'author')
    ordering = ('-created_at',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name', 'description')
    ordering = ('name',)