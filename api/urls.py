from django.urls import path, include
from rest_framework import routers
from .views import ArticleViewSet, FileViewSet

router = routers.DefaultRouter()
router.register(r'articles', ArticleViewSet)
router.register(r'files', FileViewSet)

urlpatterns = [
    path('', include(router.urls))
]
