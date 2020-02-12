import logging
import json
from author.models import Author
from book.models import Book
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.conf import settings

_logger = logging.getLogger(__name__)

client = APIClient()
BASE_URL = "/{}".format(settings.API_BASE_PATH)


class BookTestCase(APITestCase):

    def setUp(self):
        self.url_book = BASE_URL + "book/"
        self.author = Author.objects.create(name='Rodrigo Ferreira')
        self.author.save()

        self.book = Book.objects.create(
            name='Livro Pyhton', edition='1', publication_year=2020)
        self.book.save()

        qry_authors = Author.objects.all()
        authors = qry_authors.filter(id=self.author.id)
        self.book.author_ids.add(*authors)

    def test_get(self):
        response = client.get(self.url_book, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response_error = client.get(self.url_book + "1", format='json')
        self.assertEqual(response_error.status_code,
                         status.HTTP_301_MOVED_PERMANENTLY)

    def test_post(self):
        data = {
            "name": "Python Fluente 89",
            "edition": "1",
            "publication_year": 2019,
            "author_ids": [self.author.id]
        }

        response = client.post(self.url_book, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_patch_delete(self):
        data = {
            'name': 'Teste Name Book'
        }
        response_patch = client.patch(
            "{}{}/".format(self.url_book, self.book.id), data=data, format='json')
        self.assertEqual(response_patch.status_code, status.HTTP_200_OK)

        responde_del = client.delete("{}{}/".format(self.url_book, self.book.id),
                                     format='json', secure=True)
        self.assertEqual(responde_del.status_code, status.HTTP_204_NO_CONTENT)
