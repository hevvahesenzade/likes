from django.contrib import admin
from .models import Post, Comment

class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'post', 'content', 'active', 'created_at')
    list_filter = ('active', 'created_at')
    search_fields = ('user__username', 'content')

admin.site.register(Post)
admin.site.register(Comment, CommentAdmin)


