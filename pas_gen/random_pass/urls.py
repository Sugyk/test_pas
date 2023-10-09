from django.urls import path
from .views import rand_com, auth_pas, UserCreateView, LoginUser

urlpatterns = [
    path('ran', rand_com),
    path('auth_pas', auth_pas, name='a_pass'),

    path('reg/', UserCreateView.as_view(), name='reg'),
    path('accounts/login/', LoginUser.as_view(), name='login'),
]