from django.db import models

# Create your models here.

from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    pages = models.PositiveIntegerField()
    cover_image = models.ImageField(upload_to='book_covers/', blank=True, null=True)
    price = models.PositiveIntegerField()

    def __str__(self):
        return self.title


class Paper(models.Model):
    title = models.CharField(max_length=100)
    format = models.CharField(max_length=3)
    weight = models.PositiveIntegerField()
    number_of_sheets = models.PositiveIntegerField()
    cover_image = models.ImageField(upload_to='papers_cover/', blank=True, null=True)
    price = models.PositiveIntegerField()

    def __str__(self):
        return self.title
