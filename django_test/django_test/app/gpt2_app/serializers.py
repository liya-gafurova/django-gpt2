from rest_framework import serializers
from django_test.app.gpt2_app.models import *

class PostsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('title', 'text')

class PostDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'