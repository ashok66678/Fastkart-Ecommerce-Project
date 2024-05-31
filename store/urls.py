from django.urls import path
from . views import *

urlpatterns = [
    path('search/',search, name='search'),
    path("about/", about, name='about'),
    path("product/<slug:prod_slug>/",product_detail, name= "product_detail"),
    path("<slug:cate_slug>/", filter, name="filter"),
    path("", home, name = 'home'),

]