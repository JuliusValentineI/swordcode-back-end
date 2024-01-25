from rest_framework import serializers
from .models import Article, File

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'
        

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = '__all__'

