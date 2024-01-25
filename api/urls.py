from django.urls import path, include
from rest_framework import routers
from .views import PostsRepositoryViewSet

router = routers.DefaultRouter()
router.register(r'postsRepository', PostsRepositoryViewSet)

urlpatterns = [
    path('', include(router.urls))
]
