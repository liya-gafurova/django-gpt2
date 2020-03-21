from django.http import HttpResponse
from django.shortcuts import render
import numpy as np
from django_test.app.gpt2_app.models import *
from rest_framework import  generics
from django_test.app.gpt2_app.serializers import *

# Create your views here.
def myFirstView(request):
    number = np.random.random_integers(5)
    posts = Post.objects.all()
    context= {
        'posts' : posts
    }

    return  render(request, "index.html", context= context)

class PostListAll(generics.ListAPIView):
    serializer_class = PostsListSerializer
    queryset = Post.objects.all()

class PostCreateView(generics.CreateAPIView):
    # сразу надо написать serrializer class
    serializer_class = PostDetailSerializer

class PostUpdateView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PostDetailSerializer
    queryset = Post.objects.all()