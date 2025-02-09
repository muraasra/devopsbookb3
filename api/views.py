from django.shortcuts import render
from django.http import JsonResponse
from .models import Book,Author
from.serializer import BookSerializer, AuthorSerializer

from rest_framework import viewsets,filters

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    # filter_backends = [filters.SearchFilter]
    
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # filter_backends = [filters.SearchFilter]
    # search_fields = ['title', 'author']





# def index   (request):
#     return JsonResponse({'message':"Hello, world. You're at the DevOpsbook API index."})
# def book_list (request):
#     if request.method == 'GET':
#         books= Book.objects.all()
#         serializer = BookSerializer(books, many=True)
#         return JsonResponse(serializer.data, safe=False)
#     elif request.method == 'POST':
#         serializer = BookSerializer(data=request.POST)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)
    
# Create your views here.
