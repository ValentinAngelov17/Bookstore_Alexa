from django.contrib import admin
from .models import Book, Paper, OfficeSupplies, Gifts, HobbyArt, Cart, CartItem
from .forms import BookForm, PaperForm, OfficeSuppliesForm, GiftsForm, HobbyArtForm


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    form = BookForm
    list_display = ('title', 'author', 'pages')


@admin.register(Paper)
class PaperAdmin(admin.ModelAdmin):
    form = PaperForm
    list_display = ('id', 'title', 'format', 'number_of_sheets', 'weight', 'price')


@admin.register(OfficeSupplies)
class OfficeSuppliesAdmin(admin.ModelAdmin):
    form = OfficeSuppliesForm
    list_display = ('title', 'supplies', 'price')


@admin.register(Gifts)
class GiftsAdmin(admin.ModelAdmin):
    form = GiftsForm
    list_display = ('title', 'category', 'price')


@admin.register(HobbyArt)
class HobbyArtAdmin(admin.ModelAdmin):
    form = HobbyArtForm
    list_display = ('title', 'category', 'author', 'price')


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_at')


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('cart', 'product_model')
