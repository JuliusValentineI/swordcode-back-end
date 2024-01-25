#from django.shortcuts import render
from rest_framework import viewsets
#from rest_framework.response import Response
from .models import Articles, Files
from .serialize import ArticlesSerializer, FilesSerializer
"""
--- PostsRepository methods 
--- Views in database created's
"""
    
class ArticlesViewSet(viewsets.ModelViewSet):
    queryset = Articles.objects.all()
    serializer_class = ArticlesSerializer
    

class FilesViewSet(viewsets.ModelViewSet):
    queryset = Files.objects.all()
    serializer_class = FilesSerializer
    
