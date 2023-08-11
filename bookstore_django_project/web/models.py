from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.apps import apps

from bookstore_django_project.auth_web.models import AppUser


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    email = models.EmailField()
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    address = models.TextField(blank=True)
    order_number = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.pk} - {self.email}"


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    pages = models.PositiveIntegerField()
    cover_image = models.ImageField(upload_to='book_covers/', blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.title


class Paper(models.Model):
    title = models.CharField(max_length=100)
    format = models.CharField(max_length=3)
    weight = models.PositiveIntegerField()
    number_of_sheets = models.PositiveIntegerField()
    cover_image = models.ImageField(upload_to='papers_cover/', blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

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

    title = models.CharField(
        blank=False,
        null=False,
    )

    cover_image = models.ImageField(upload_to='office_covers/', blank=True, null=True)

    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.get_supplies_display()


class Gifts(models.Model):
    GIFTS = "gifts"
    OTHER = "other"

    CATEGORY_CHOICES = [
        (GIFTS, 'подаръци'),
        (OTHER, 'сувенири'),
    ]

    title = models.CharField(max_length=100)

    category = models.CharField(
        max_length=100,
        choices=CATEGORY_CHOICES,
    )

    cover_image = models.ImageField(upload_to='gifts_cover/', blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

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

    title = models.CharField(max_length=100)

    category = models.CharField(
        max_length=100,
        choices=CATEGORY_CHOICES,
    )

    author = models.CharField(max_length=100)

    cover_image = models.ImageField(upload_to='hobby_art_covers/', blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.get_category_display()


class Cart(models.Model):
    user = models.ForeignKey(AppUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Cart for {self.user.email}"


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    product_model = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField(default=1)

    # product = models.ForeignKey(Book, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.product_model}"

    @property
    def product(self):
        content_type = ContentType.objects.get(model=self.product_model)
        model_class = content_type.model_class()
        return model_class.objects.get(id=self.object_id)
