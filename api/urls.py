from django.urls import path, include
from rest_framework import routers
from .views import ArticlesViewSet, FilesViewSet

router = routers.DefaultRouter()
router.register(r'articles', ArticlesViewSet)
router.register(r'files', FilesViewSet)

urlpatterns = [
    path('', include(router.urls))
]
