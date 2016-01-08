
from django.contrib import admin
from .models import Post,Comment
from django.contrib import admin
from embed_video.admin import AdminVideoMixin




class Inline(admin.StackedInline):
    model = Comment
    extra = 2

class PostAdmin(admin.ModelAdmin, AdminVideoMixin):
    fields = ['author', 'title', 'text', 'image', 'created_date', 'published_date', 'video']
    inlines = [Inline]
    list_filter = ['title', 'created_date']


admin.site.register(Post, PostAdmin)
