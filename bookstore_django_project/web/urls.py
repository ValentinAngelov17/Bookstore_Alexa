from django.urls import path

from bookstore_django_project.web.views import IndexView, AboutView, PaperView, OfficeProductsView, HobbyArtView, \
    BooksView, GiftsView, add_to_cart, shopping_cart, remove_cart_item

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('about/', AboutView.as_view(), name='about'),
    path('paper/', PaperView.as_view(), name='paper'),
    path('office/', OfficeProductsView.as_view(), name='office'),
    path('hobby-art/', HobbyArtView.as_view(), name='hobby art'),
    path('books/', BooksView.as_view(), name='books'),
    path('gifts/', GiftsView.as_view(), name='gifts'),
    path('shopping-cart/', shopping_cart, name='shopping cart'),
    path('add-shopping-cart/', add_to_cart, name='add shopping cart'),
    path('remove_cart_item/<int:pk>/', remove_cart_item, name='remove cart item')

]
# Ang3loviC!
