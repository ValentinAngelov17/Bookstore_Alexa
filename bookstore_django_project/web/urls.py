from django.urls import path

from bookstore_django_project.web.views import IndexView, AboutView, PaperView, OfficeProductsView, HobbyArtView, \
    BooksView, GiftsView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('about/', AboutView.as_view(), name='about'),
    path('paper/', PaperView.as_view(), name='paper'),
    path('office/', OfficeProductsView.as_view(), name='office'),
    path('hobby-art/', HobbyArtView.as_view(), name='hobby art'),
    path('books/', BooksView.as_view(), name='books'),
    path('gifts/', GiftsView.as_view(), name='gifts'),

]
# Ang3loviC!
