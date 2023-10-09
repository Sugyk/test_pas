from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from random import choices
from django.urls import reverse_lazy
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.views.generic.edit import CreateView


def rand_com(request):
    new_pas = ''.join([str(i) for i in choices(population=range(10), k=4)])
    return HttpResponse(f'{new_pas}')

@login_required
def auth_pas(request):
    new_pas = ''.join([str(i) for i in choices(population=range(10), k=4)])
    response = HttpResponse(f'{new_pas}')
    logout(request)
    return response


class UserCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    template_name = 'random_pass/registration.html'
    success_url = reverse_lazy('car_list')


class LoginUser(LoginView):
    template_name = 'random_pass/login.html'
    form_class = AuthenticationForm
    redirect_authenticated_user = True
    next_page = reverse_lazy('a_pass')
