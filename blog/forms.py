# -*- coding: utf-8 -*-

from django import forms
from .models import Post, Comment, Tag
from embed_video.admin import AdminVideoMixin


class PostForm(forms.ModelForm, AdminVideoMixin):

    class Meta:
        model = Post
        fields = ('title', 'image', 'video', 'text', 'tags')
        filter_horizontal = ['tags']


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text')



class TagForm(forms.ModelForm):

    class Meta:
        model = Tag
        fields = ('tag',)