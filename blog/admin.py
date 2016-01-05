
from django.contrib import admin
from .models import Post,Comment


class Inline(admin.StackedInline):
    model = Comment
    extra = 2

class PostAdmin(admin.ModelAdmin):
    fields = ['author', 'title', 'text', 'image', 'created_date', 'published_date']
    inlines = [Inline]
    list_filter = ['title', 'created_date']


admin.site.register(Post, PostAdmin)
