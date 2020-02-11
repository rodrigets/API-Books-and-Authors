from django.db import models
from author.models import Author
import datetime

def year_choices():
    """ Years generator method
    """
    return [(str(r),str(r)) for r in range(1800, datetime.date.today().year+1)]

def current_year():
    """ Method to generate current year
    """
    return str(datetime.date.today().year)


class Book(models.Model):

    name = models.CharField(max_length=100, verbose_name='Name')
    edition = models.CharField(max_length=20, verbose_name='Edition')
    publication_year = models.CharField(max_length=4,blank=True, null=True,
        choices=year_choices(), default=current_year())
    author_ids = models.ManyToManyField(Author)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
