from django.urls import path
from .views import *

urlpatterns = [
    path('',card_page, name='card_page'),
]