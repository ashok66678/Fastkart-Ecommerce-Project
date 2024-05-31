from django.shortcuts import render, redirect
from .models import Cart
from store.models import Product
from .utils import cartCount
# Create your views here.

def cart(request):
    if request.user.is_authenticated:
        cart_data = cartCount(request)
        context = {'cart_data':cart_data['cart_data'],'total':round(cart_data['total_cart_value'],3),'cart_count':cart_data['cart_count']}
        return render(request, "cart.html",context)
    else:
        return redirect('/account/login/?next='+request.META.get('HTTP_REFERER'))


def addToCart(request,item_id):
    
    if request.user.is_authenticated:
        product = Product.objects.get(id=item_id)

        try:
            data = Cart.objects.get(user=request.user, product=product)
            data.quantity = data.quantity + 1
            data.save()

        except Cart.DoesNotExist:
            Cart(user=request.user, product=product,quantity=1).save()

        return redirect(request.META.get('HTTP_REFERER'))   
    
    else:
        return redirect('/account/login/?next='+request.META.get('HTTP_REFERER'))
    


def addQuantity(request,id):
    if request.user.is_authenticated:
        cart = Cart.objects.get(id=id)
        cart.quantity = int(cart.quantity) + 1
        cart.save()
        return redirect(request.META.get('HTTP_REFERER'))
    else:
        return redirect('/')
    

def removeQuantity(request,id):
    if request.user.is_authenticated:
        cart = Cart.objects.get(id=id)
        if cart.quantity > 1:
            cart.quantity = int(cart.quantity) - 1
            cart.save()
        # else:
            # cart.delete()
        return redirect(request.META.get('HTTP_REFERER'))
    else:
        return redirect('/')
    


def removeItemFromCart(request, item_id):
    if request.user.is_authenticated:
        try:
            cart_item = Cart.objects.get(id=item_id)
            cart_item.delete()
        except Cart.DoesNotExist:
            pass  # Handle the case where the cart item does not exist (optional)
        return redirect(request.META.get('HTTP_REFERER'))
    else:
        return redirect('/account/login/?next=' + request.META.get('HTTP_REFERER'))
