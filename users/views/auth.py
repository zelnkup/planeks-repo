from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import View
from django.contrib.auth.views import auth_logout

from users.forms.login import UserAuthForm


class UserLoginView(LoginView):
    """
    Форма логина пользователя
    """

    form_class = UserAuthForm
    template_name = "login.html"
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy("users:index")


class LogoutView(View):
    """
    Форма логаута пользователя
    """

    def get(self, request, *args, **kwargs):
        auth_logout(request)
        return HttpResponseRedirect(reverse_lazy("users:login"))
