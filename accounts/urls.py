from django.urls import path
from .views import *

urlpatterns = [
    path('',Login_page, name='login_page'),
    path('forget-page/',Forget_page, name='forget_page'),
    path('register-page/',Register_page, name='register_page'),
    path('logout/',Logout_page, name='logout_page'),
]



