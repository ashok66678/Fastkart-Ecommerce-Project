from django.urls import path
from .views import *

urlpatterns = [
    path("",checkout,name="checkout"),
    path('make-order/',makeOrder,name='make-order')
]