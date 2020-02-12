import json
from .models import Author
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.conf import settings

client = APIClient()



class AuthorTestCase(APITestCase):

    def test_get_author(self):

        response = client.get("/" + settings.API_BASE_PATH + "author/", format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response_error = client.get("/" + settings.API_BASE_PATH + "author/1", format='json')
        self.assertEqual(response_error.status_code, status.HTTP_301_MOVED_PERMANENTLY)
