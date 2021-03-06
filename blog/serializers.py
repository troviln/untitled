from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Chat


class ChatSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        queryset=User.objects.all(), slug_field='username'
    )
    class Meta:
        model = Chat
        fields = ('id', 'author', 'text', 'created', 'updated')