# -*- coding: utf-8 -*-

from django import forms
from .models import Post, Comment
from embed_video.admin import AdminVideoMixin


class PostForm(forms.ModelForm, AdminVideoMixin):

    class Meta:
        model = Post
        fields = ('title', 'image', 'video', 'text',)

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)