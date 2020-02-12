import json
from django.http import HttpResponse
from rest_framework.viewsets import ModelViewSet
from ..models import Book, Author
from .serializers import BookSerializer


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def validate_instance_request(self, data, required_fields):
        """ Validator for fields required
        """
        error_fields = [
            field for field in required_fields if field not in data]
        return error_fields

    def return_error_http(self, http_code, msg):
        """ Error return handling
        """
        return HttpResponse(json.dumps({"result": "Error", "message": msg}),
                            status=http_code,
                            content_type="application/json")

    def get_queryset(self):
        """Responsible for method get, 
        with possible filter for many fields
        """
        queryset = Book.objects.all()

        name = self.request.query_params.get('name', None)

        publication_year = self.request.query_params.get(
            'publication_year', None)

        edition = self.request.query_params.get('edition', None)

        author_ids = self.request.query_params.get('author_ids', None)

        if name:
            queryset = queryset.filter(name=name)
        if publication_year:
            queryset = queryset.filter(publication_year=publication_year)
        if edition:
            queryset = queryset.filter(edition=edition)
        if author_ids:
            queryset = queryset.filter(author_ids=author_ids)

        return queryset

    def create(self, request, *args, **kwargs):
        """ Responsible for created the book register 
        """
        queryset = Book.objects.all()

        required_fields = ['name', 'edition', 'publication_year', 'author_ids']
        has_errors = self.validate_instance_request(
            request.data, required_fields)

        if has_errors:
            message = ('Field(s) %s required' % ', '.join(has_errors))
            return self.return_error_http(308, message)

        books = queryset.filter(name=request.data.get('name'))
        book = books[0] if len(books) > 0 else []

        if book:
            return HttpResponse("The informed book is already registered.",
                                status=308,
                                content_type="application/json")
        else:
            abook = Book.objects.create(
                name=request.data.get('name'),
                publication_year=request.data.get('publication_year'),
                edition=request.data.get('edition'),
            )
            qry_authors = Author.objects.all()
            authors = qry_authors.filter(id__in=request.data.get('author_ids'))
            abook.author_ids.add(*authors)

        return HttpResponse(
            json.dumps(BookSerializer(abook).data),
            status=200,
            content_type="application/json")

    def partial_update(self, request, *args, **kwargs):
        return super(BookViewSet, self).partial_update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super(BookViewSet, self).destroy(request, *args, **kwargs)
