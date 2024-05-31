from django.shortcuts import render
from store.models import *
from cart.utils import cartCount
from django.db.models import Q

from django import template
register = template.Library()



# def funcName():
#   logic here
@register.simple_tag
def head_category():
    allcategory = Category.objects.all()[:5] 
    # context = {'allcategory': allcategory}
    return allcategory
