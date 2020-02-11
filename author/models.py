from django.db import models

class Author(models.Model):

    name = models.CharField(max_length=30, verbose_name='Name')

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
