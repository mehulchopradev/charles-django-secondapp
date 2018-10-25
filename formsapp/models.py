from django.db import models
from django.urls import reverse

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=30)
    pages = models.IntegerField()
    price = models.FloatField(null=True, blank=True)
    publisheddate = models.DateField(null=True, blank=True)

class Author(models.Model):
    name = models.CharField(max_length=30)
    ratings = models.IntegerField()

    def get_absolute_url(self):
        return reverse('author-detail', kwargs={'author_id': self.pk})

    def __str__(self):
        return self.name
