from django.contrib.auth.decorators import login_required
from django.contrib.contenttypes.models import ContentType
from django.core.paginator import Paginator, Page
from django.http import HttpResponseBadRequest, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View

from django.views.generic import ListView

from .forms import OrderForm
from .models import Book, Paper, OfficeSupplies, Gifts, HobbyArt, Cart, CartItem, Order
from django.apps import apps


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


class OfficeProductsView(ListView):
    model = OfficeSupplies
    template_name = 'products/office_products.html'
    context_object_name = 'office_supplies'
    paginate_by = 8


class HobbyArtView(ListView):
    model = HobbyArt
    template_name = 'products/hobby_and_art.html'
    context_object_name = 'hobby_arts'
    paginate_by = 8


class BooksView(ListView):
    model = Book
    template_name = 'products/books.html'
    context_object_name = 'books'
    paginate_by = 10


class GiftsView(ListView):
    model = Gifts
    template_name = 'products/gifts.html'
    context_object_name = 'gifts'
    paginate_by = 8


@login_required
def add_to_cart(request):
    if request.method == 'POST':
        user = request.user
        if Cart.objects.filter(user=request.user).exists():
            cart = Cart.objects.get(user=request.user)
        else:
            cart = Cart.objects.create(user=request.user)

        product_model = request.POST.get('product_model')
        product_id = request.POST.get('product_id')

        if product_model and product_id:
            print(product_model)
            print(product_id)
            content_type = ContentType.objects.get(model=product_model.lower())
            product = content_type.get_object_for_this_type(id=product_id)

            cart_items = CartItem.objects.filter(cart=cart)

            try:
                product = cart_items.get(object_id=product_id, product_model=product_model,
                                         content_type=content_type)
                product.quantity += int(request.POST['quantity'])
                product.save()
            except:
                CartItem.objects.create(cart=cart, product_model=product_model, content_type=content_type,
                                        object_id=product_id, quantity=request.POST['quantity'])

            # return redirect('books')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            return HttpResponseBadRequest("Invalid request data")
    else:
        return HttpResponseBadRequest("Invalid request method")


@login_required
def shopping_cart(request):
    user = request.user
    cart, created = Cart.objects.get_or_create(user=user)
    cart_items = cart.cartitem_set.all()

    context = {
        'cart_items': cart_items,
        'cart': cart,
    }

    return render(request, 'shopping/shopping_cart.html', context)


def remove_cart_item(request, pk):
    CartItem.objects.get(pk=pk).delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def create_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.save()

            return redirect('order details', order_id=order.id)
    else:

        initial_data = {
            'email': request.user.email,
            'first_name': request.user.first_name if request.user.first_name else '',
            'last_name': request.user.last_name if request.user.last_name else '',
        }
        form = OrderForm(initial=initial_data)

    user = request.user
    cart, created = Cart.objects.get_or_create(user=user)
    cart_items = cart.cartitem_set.all()

    context = {
        'cart_items': cart_items,
        'cart': cart,
        'form': form,
    }

    return render(request, 'shopping/create_order.html', context)


@login_required
def order_details(request, order_id):
    order = get_object_or_404(Order, id=order_id)

    context = {
        'order': order,
    }

    return render(request, 'shopping/order_details.html', context)


@login_required
def order_history(request):
    user = request.user
    orders = Order.objects.filter(user=user).order_by('created_at')

    context = {
        'orders': orders,
    }

    return render(request, 'shopping/order_history.html', context)
