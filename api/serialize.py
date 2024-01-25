from rest_framework import serializers
from .models import Articles, Files

class ArticlesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Articles
        fields = '__all__'
        

class FilesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Files
        fields = '__all__'

