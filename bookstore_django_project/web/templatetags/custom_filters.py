from django import template

from bookstore_django_project.web.models import Book, Paper, OfficeSupplies, HobbyArt, Gifts

register = template.Library()


@register.simple_tag(name='return_product')
def return_product(product_type, product_id, get_item):
    if product_type == 'Book':
        book = Book.objects.get(pk=int(product_id))
        if get_item == 'title':
            return book.title
        elif get_item == 'price':
            return book.price
    elif product_type == 'Paper':
        paper = Paper.objects.get(pk=int(product_id))
        if get_item == 'title':
            return paper.title
        elif get_item == 'price':
            return paper.price
    elif product_type == 'OfficeSupplies':
        office = OfficeSupplies.objects.get(pk=int(product_id))
        if get_item == 'title':
            return office.title
        elif get_item == 'price':
            return office.price
    elif product_type == 'HobbyArt':
        hobby_art = HobbyArt.objects.get(pk=int(product_id))
        if get_item == 'title':
            return hobby_art.title
        elif get_item == 'price':
            return hobby_art.price
    elif product_type == 'Gifts':
        gifts = Gifts.objects.get(pk=int(product_id))
        if get_item == 'title':
            return gifts.title
        elif get_item == 'price':
            return gifts.price


@register.simple_tag(name='product_total_price')
def product_total_price(product_type, product_id, quantity):
    if product_type == 'Book':
        return f"{(Book.objects.get(pk=int(product_id)).price * quantity):.02f}"
    elif product_type == 'Paper':
        return f"{(Paper.objects.get(pk=int(product_id)).price * quantity):.02f}"
    elif product_type == 'OfficeSupplies':
        return f"{(OfficeSupplies.objects.get(pk=int(product_id)).price * quantity):.02f}"
    elif product_type == 'HobbyArt':
        return f"{(HobbyArt.objects.get(pk=int(product_id)).price * quantity):.02f}"
    elif product_type == 'Gifts':
        return f"{(Gifts.objects.get(pk=int(product_id)).price * quantity):.02f}"


@register.simple_tag(name='cart_total')
def cart_total(cart_items):
    total = 0
    for item in cart_items:
        if item.product_model == 'Book':
            product = Book.objects.get(pk=item.object_id)
        elif item.product_model == 'Paper':
            product = Paper.objects.get(pk=item.object_id)
        elif item.product_model == 'OfficeSupplies':
            product = OfficeSupplies.objects.get(pk=item.object_id)
        elif item.product_model == 'HobbyArt':
            product = HobbyArt.objects.get(pk=item.object_id)
        elif item.product_model == 'Gifts':
            product = Gifts.objects.get(pk=item.object_id)

        total += float(product.price * item.quantity)

    return f"{total:.02f}"


@register.filter(name='get_product')
def get_product(cart_item):
    return cart_item.product
