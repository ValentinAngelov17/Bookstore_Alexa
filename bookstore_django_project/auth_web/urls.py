# auth urls
from django.urls import path

from bookstore_django_project.auth_web.views import LoginUserView, RegisterUserView, LogoutUserView, UserDetailsView

urlpatterns = [
    path('login/', LoginUserView.as_view(), name='login'),
    path('register/', RegisterUserView.as_view(), name='register'),
    path('logout/', LogoutUserView.as_view(), name='logout'),
    path('user/<int:pk>/', UserDetailsView.as_view(), name='user details'),
]
