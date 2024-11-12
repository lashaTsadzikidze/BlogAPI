from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'author', views.AuthorViewSet),
router.register(r'blog', views.BlogViewSet),

urlpatterns = [
    path('', include(router.urls)),
]