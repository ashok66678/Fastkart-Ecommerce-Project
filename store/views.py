from django.shortcuts import render
from . models import *
from cart.utils import cartCount
from django.db.models import Q

# Create your views here.

# def home(request):
#     context = {}
#     return render(request, "home.html")

def home(request):
    trend_view = Product.objects.all().order_by('-page_views')[:6]    ## ADDED
    if request.user.is_authenticated:
        cart_data = cartCount(request)
        products = Product.objects.all()[:12]
        context= {'cart_count':cart_data['cart_count'], 'product_data': products,'trend_view':trend_view}
        return render(request, "home.html", context)
    else:
        products = Product.objects.all()[:12]
        return render(request, "home.html" ,context={'cart_count':0,'product_data': products,'trend_view':trend_view})

def about(request):
    return render(request, "about.html" ,)


def filter(request, cate_slug):
    try:
        pricing = request.GET['price'].split('-')
        print() 
        category = Category.objects.get(slug = cate_slug)
        products = Product.objects.filter(selling_price__gte=pricing[0], selling_price__lte=pricing[1],category = category)
    except:
        category = Category.objects.get(slug = cate_slug)
        products = Product.objects.filter(category = category)

    ## For cart update on the Navbar
    if request.user.is_authenticated:
        cart_data = cartCount(request)
        allcategory =Category.objects.all()
        context= {'product_data': products,'cart_count':cart_data['cart_count'], 'allcategory':allcategory}
        return render(request, "filter.html", context)
    else:
        allcategory =Category.objects.all()
        context= {'product_data': products, 'cart_count':0, 'allcategory':allcategory}
        return render(request, "filter.html", context)


def product_detail(request, prod_slug): 
    product = Product.objects.get(slug=prod_slug) 
    if request.user.is_authenticated:
        cart_data = cartCount(request)
    else:
        cart_data = {'cart_count':0} 
    context= {"product":product, "cart_count":cart_data['cart_count']} 
    product.page_views = product.page_views + 1      ## NEW ADDED
    product.save() 
    return render(request, "product_detail.html", context)


def search(request):
    search_value = request.GET['q']
    allcategory =Category.objects.all()
    try:
        pricing = request.GET['price'].split('-')
        products = Product.objects.filter(Q(title__icontains=search_value) | Q(description__icontains=search_value),selling_price__gte=pricing[0], selling_price__lte=pricing[1])
    except:
        products = Product.objects.filter(Q(title__icontains=search_value) | Q(description__icontains=search_value))
    if request.user.is_authenticated:
        cart_data = cartCount(request)
    else: 
        cart_data = {'cart_count':0}
    
    context= {"product_data":products, 'allcategory':allcategory, "cart_count":cart_data['cart_count'],'searchpage':search_value}
    return render(request, 'filter.html' ,  context)



def head_category(request):
    allcategory = Category.objects.all() 
    context = {'allcategory': allcategory}
    return render(request, 'main.html', context)
