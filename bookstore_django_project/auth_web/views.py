from django import forms
from django.contrib.auth import views as auth_views, login, get_user_model
from django.contrib.auth import forms as auth_forms
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import mixins as auth_mixins
from django.utils.translation import gettext_lazy as _

# Create your views here.
UserModel = get_user_model()


class RegisterUserForm(auth_forms.UserCreationForm):
    password2 = forms.CharField(
        label=_("Repeat Password"),
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        strip=False,
        help_text=_(""),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].help_text = _('')

    class Meta(auth_forms.UserCreationForm.Meta):
        model = UserModel
        fields = ('email',)


class RegisterUserView(views.CreateView):
    template_name = 'registration.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, self.object)

        return result


class LoginUserView(auth_views.LoginView):
    template_name = 'login.html'


class LogoutUserView(auth_views.LogoutView):
    pass


class UserDetailsView(auth_mixins.LoginRequiredMixin, views.DetailView):
    model = UserModel
    template_name = 'user_details.html'
