from django.shortcuts import render
from rest_framework import viewsets
from .serialize import PostsRepositorySerializer
from .models import PostsRepository

class PostsRepositoryViewSet(viewsets.ModelViewSet):
    queryset = PostsRepository.objects.all()
    serializer_class = PostsRepositorySerializer
