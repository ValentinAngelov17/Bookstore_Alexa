from django.contrib import admin
from .models import Book, Paper
from .forms import BookForm


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    form = BookForm
    list_display = ('title', 'author', 'pages')


@admin.register(Paper)
class BookAdmin(admin.ModelAdmin):
    form = BookForm
    list_display = ('title', 'format', 'number_of_sheets', 'weight', 'price')
