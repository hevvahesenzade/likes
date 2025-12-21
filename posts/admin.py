from django.contrib import admin
from .models import Post, Comment

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'timestamp', 'featured', 'total_likes')
    list_filter = ('featured', 'timestamp', 'author')
    search_fields = ('title', 'overview', 'content')

    def total_likes(self, obj):
        return obj.likes.count()
    total_likes.short_description = 'Likes'


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'post', 'content', 'active', 'created_at')
    list_filter = ('active', 'created_at')
    search_fields = ('user__username', 'content')


