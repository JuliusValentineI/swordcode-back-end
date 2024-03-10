from django.urls import path, include
from rest_framework import routers
from .views import ArticlesViewSet, FilesViewSet, showFile, dataArticle

router = routers.DefaultRouter()
router.register(r'articles', ArticlesViewSet)
router.register(r'files', FilesViewSet)

urlpatterns = [
    path('showFile/', showFile, name="Show"),
    path('dataArticle/', dataArticle, name="Article"),
    path('', include(router.urls)),
]
