from django.shortcuts import render
from rest_framework import viewsets
from .serializers import AuthorSerializer, BlogSerializer
from .models import Author, Blog


# Create your views here.
class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
