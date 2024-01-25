from rest_framework import serializers
from .models import PostsRepository

class PostsRepositorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PostsRepository
        fields = '__all__'
