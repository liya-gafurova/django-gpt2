from django.contrib import admin
from django.urls import path, include
from gpt2_sciq.app.gpt2_distractor_generation.views import   *

urlpatterns = [
    path('create/', generate_distractor)
]
