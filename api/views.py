#from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework import viewsets
#from rest_framework.mixins import Response
#from rest_framework.response import Response
from .models import Articles, Files
from .serialize import ArticlesSerializer, FilesSerializer
"""
--- Article and views methods 
--- Views in database created's
"""
    
class ArticlesViewSet(viewsets.ModelViewSet):
    queryset = Articles.objects.all()
    serializer_class = ArticlesSerializer
    

class FilesViewSet(viewsets.ModelViewSet):
    queryset = Files.objects.all()
    serializer_class = FilesSerializer
    

def showFile(request):
    try:
        articleId = int(request.GET['article'])
        file = Files.objects.filter(article=articleId).first()

        data = {
            "id": file.id,
            "filename": file.filename,
            "filetype": file.filetype,
            "content": file.content,
            "article": articleId
        }

        if file == None:
            return JsonResponse({"error": "File not found"})
       
        return JsonResponse(data)
    except ValueError:
        return JsonResponse({"error": "Invalid article id format"})

def dataArticle(request):
    try:
        articleId = int(request.GET['article'])
        article = Articles.objects.filter(id=articleId).first()

        data = {
            "id": article.id,
            "title": article.title,
            "description": article.description,
            "post_type": article.post_type,
            "published_at": article.published_at,
            "update_at": article.update_at,
            "is_active": article.is_active,
        }
        if article == None:
            return JsonResponse({"error": "Invalid article"})

        return JsonResponse(data)
    except ValueError:
        return JsonResponse({"error": "Invalid article id format"})

