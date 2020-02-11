import json
from django.http import HttpResponse
from rest_framework.viewsets import ModelViewSet
from ..models import Author
from .serializers import AuthorSerializer


class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    def get_queryset(self):
        """Responsible for method get, 
        with possible filter for name field
        """
        queryset = Author.objects.all()
        name = self.request.query_params.get('name', None)
        if name:
            queryset = queryset.filter(name=name)
        return queryset
