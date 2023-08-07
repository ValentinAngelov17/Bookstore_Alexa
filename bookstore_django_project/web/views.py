from django.core.paginator import Paginator, Page
from django.shortcuts import render
from django.views import View

from django.views.generic import ListView
from .models import Book, Paper, OfficeSupplies, Gifts, HobbyArt


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


class OfficeProductsView(ListView):
    model = OfficeSupplies
    template_name = 'products/office_products.html'
    context_object_name = 'office_supplies'
    paginate_by = 8

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_paginated'] = context['page_obj'].paginator.num_pages > 1
        return context


class HobbyArtView(ListView):
    model = HobbyArt
    template_name = 'products/hobby_and_art.html'
    context_object_name = 'hobby_arts'
    paginate_by = 8

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_paginated'] = context['page_obj'].paginator.num_pages > 1
        return context


class BooksView(ListView):
    model = Book
    template_name = 'products/books.html'
    context_object_name = 'books'
    paginate_by = 8

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_paginated'] = context['page_obj'].paginator.num_pages > 1
        return context


class GiftsView(ListView):
    model = Gifts
    template_name = 'products/gifts.html'
    context_object_name = 'gifts'
    paginate_by = 8

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_paginated'] = context['page_obj'].paginator.num_pages > 1
        return context
