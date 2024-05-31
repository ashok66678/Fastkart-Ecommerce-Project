# from django.contrib import admin
from django.urls import path
from .views import * 

urlpatterns = [
    path("",cart,name="cart"),
    path('add-to-cart/<int:item_id>/',addToCart,name="add-to-cart"),
    path('increase-quantity/<int:id>/',addQuantity, name='increase-quantity'),
    path('decrease-quantity/<int:id>/',removeQuantity, name="decrease-quantity"), 
    path('remove-item/<int:item_id>/', removeItemFromCart, name='remove-item-cart'),
]