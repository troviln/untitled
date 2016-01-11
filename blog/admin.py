
from django.contrib import admin
from .models import Post, Comment, Tag, Chat
from django.contrib import admin
from embed_video.admin import AdminVideoMixin


class TagAdmin(admin.ModelAdmin):
    model = Tag


class Inline(admin.StackedInline):
    model = Comment
    extra = 1

class PostAdmin(admin.ModelAdmin, AdminVideoMixin):
    fields = ['author', 'title', 'tags', 'text', 'image', 'created_date', 'published_date', 'video']
    inlines = [Inline]
    ordering = ['-created_date']
    list_filter = ['title', 'created_date']
    filter_horizontal = ['tags']


admin.site.register(Post, PostAdmin)
admin.site.register(Tag)
admin.site.register(Chat)