from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from author.api.serializers import AuthorSerializer
from ..models import Book


class BookSerializer(ModelSerializer):
    author_ids = AuthorSerializer(many=True, read_only=True)
    
    class Meta:
        model = Book
        fields = '__all__'
