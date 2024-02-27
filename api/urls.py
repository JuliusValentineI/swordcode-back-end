from django.urls import path, include
from rest_framework import routers
from .views import ArticlesViewSet, FilesViewSet, showFile

router = routers.DefaultRouter()
router.register(r'articles', ArticlesViewSet)
router.register(r'files', FilesViewSet)

urlpatterns = [
    path('showFile/', showFile, name="Show"),
    path('', include(router.urls)),
]
