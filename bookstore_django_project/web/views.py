from django.core.paginator import Paginator, Page
from django.shortcuts import render
from django.views import View

from django.views.generic import ListView
from .models import Book, Paper


class IndexView(View):
    def get(self, request):
        return render(request, 'index.html')


class AboutView(View):
    def get(self, request):
        return render(request, 'about.html')


class PaperView(ListView):
    model = Paper
    template_name = 'products/paper.html'
    context_object_name = 'papers'
    paginate_by = 8

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_paginated'] = context['page_obj'].paginator.num_pages > 1
        return context


class OfficeProductsView(View):
    def get(self, request):
        return render(request, 'products/office_products.html')


class HobbyArtView(View):
    def get(self, request):
        return render(request, 'products/hobby_and_art.html')


class BooksView(ListView):
    model = Book
    template_name = 'products/books.html'
    context_object_name = 'books'
    paginate_by = 8

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_paginated'] = context['page_obj'].paginator.num_pages > 1
        return context


class GiftsView(View):
    def get(self, request):
        return render(request, 'products/gifts.html')
