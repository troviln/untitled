# -*- coding: utf-8 -*-

from django import forms
from .models import Post, Comment, Tag, Chat
from embed_video.admin import AdminVideoMixin


class PostForm(forms.ModelForm, AdminVideoMixin):
    class Meta:
        model = Post
        fields = ('title', 'image', 'video', 'text', 'tags')


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'text')


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ('tag',)


class ChatForm(forms.ModelForm):
    class Meta:
        model = Chat
        fields = ('text',)

        widgets = {

                'text': forms.Textarea(
                    attrs={'id': 'post-text', 'rows': 2,  'required': True, 'placeholder': 'Say something...'}
                ),}
