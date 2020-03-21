from django.contrib import admin
from django.urls import path
from django_test.app.gpt2_app import  views
urlpatterns = [
    path('post/create/', views.PostCreateView.as_view() ),
    path('all/', views.PostListAll.as_view()),
    path('post/update/<int:pk>', views.PostUpdateView.as_view())

]
