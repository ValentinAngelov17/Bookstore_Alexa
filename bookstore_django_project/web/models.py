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


class OfficeSupplies(models.Model):
    SCISSORS = 'scissors'
    PENS = 'pens'
    PENCILS = "pencil"
    FOLDERS = "folder"
    CORRECTORS = "corrector"
    TAPES = "tape"
    GLUES = "glue"

    CONSUMABLE_CHOICES = [
        (SCISSORS, 'ножици'),
        (PENS, 'химикалки'),
        (PENCILS, 'моливи'),
        (CORRECTORS, 'коректори'),
        (FOLDERS, 'папки'),
        (TAPES, 'тикса'),
        (GLUES, 'лепила'),

    ]

    supplies = models.CharField(
        max_length=100,
        choices=CONSUMABLE_CHOICES,
    )

    name = models.CharField(
        blank=False,
        null=False,
    )

    cover_image = models.ImageField(upload_to='office_covers/', blank=True, null=True)

    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.get_supplies_display()


class Gifts(models.Model):
    GIFTS = "gifts"
    OTHER = "other"

    CATEGORY_CHOICES = [
        (GIFTS, 'подаръци'),
        (OTHER, 'сувенири'),
    ]

    name = models.CharField(max_length=100)

    category = models.CharField(
        max_length=100,
        choices=CATEGORY_CHOICES,
    )

    cover_image = models.ImageField(upload_to='gifts_cover/', blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.get_category_display()


class HobbyArt(models.Model):
    CARDS = "cards"
    DECORATION = "decoration"
    HOMEMADE = "homemade"

    CATEGORY_CHOICES = [
        (CARDS, 'картички'),
        (DECORATION, 'декорации'),
        (HOMEMADE, 'ръчна изработка'),
    ]

    name = models.CharField(max_length=100)

    category = models.CharField(
        max_length=100,
        choices=CATEGORY_CHOICES,
    )

    author = models.CharField(max_length=100)

    cover_image = models.ImageField(upload_to='hobby_art_covers/', blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.get_category_display()
