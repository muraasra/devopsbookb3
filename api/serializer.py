from rest_framework import serializers
from .models import Book,Author


# 
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__' # afficher tous les champs de la table Book

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__' # afficher tous les champs de la table Author
        
    