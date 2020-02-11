import csv
from optparse import make_option
from ...models import Author
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):

    def handle(self, **options):
        """ Method for authors import with CSV
        """
        path = 'authors.csv'
        with open(path) as f:
            reader = csv.reader(f)
            for row in reader:
                _, created = Author.objects.get_or_create(
                    name=row[0],
                )
