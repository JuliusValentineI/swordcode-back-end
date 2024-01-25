#from django.shortcuts import render
from rest_framework import viewsets
#from rest_framework.response import Response
from .models import Article, File
from .serialize import ArticleSerializer, FileSerializer
"""
--- PostsRepository methods 
--- Views in database created's
"""
    
class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    

class FileViewSet(viewsets.ModelViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerializer
    
