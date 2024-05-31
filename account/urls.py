from django.urls import path
from . views import *

urlpatterns = [
    path("login/", login, name = 'login'),
    path("logout/", logout, name = 'logout'),
    path("register/",register,  name="register"),
    path("add_address/", addAddress, name = "add_address"),
    path("dashboard/",dashboard,  name="dashboard"),
    path("address-to-delete/<int:address_id>/",addressToDelete, name="address-to-delete"),

]