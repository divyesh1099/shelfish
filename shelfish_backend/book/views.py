from django.shortcuts import render
from .serializers import BookSerializer 
from rest_framework import viewsets      
from .models import Book
# Create your views here.
class BookView(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()