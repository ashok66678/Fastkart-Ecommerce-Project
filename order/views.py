from django.shortcuts import render, redirect
from cart.models import Cart
from account.models import ShippingAddress
from .models import Order, OrderItem
from cart.utils import cartCount

# Create your views here.
## Checkout page
def checkout(request):
    if request.user.is_authenticated:

        ## getting all the products from the cart.
        cart_data = Cart.objects.filter(user = request.user)

        ## getting  all the addresses of the user.
        if len(cart_data) > 0:
            addresses = ShippingAddress.objects.filter(customer=request.user)

            total = 0.0  ## total cart value
            for cart in cart_data:
                total = total + cart.get_total_value

            ## total number of products in the cart
            cart_count = 0
            cart = Cart.objects.filter(user = request.user)
            for ca in cart:
                cart_count += ca.quantity

            context = {'cart' :cart_data, 'total':round(total,2),'addresses':addresses,'cart_count':cart_count}
            return render(request, "checkout.html", context)
        else:
            return redirect("/")
    else:
        return redirect("/account/login.html")


## This is not any page, but the logic to get the billing address from the checkout products and make the order and empty the cart.
def makeOrder(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            shp_addr = request.POST['selected_address']
            deliver_info = request.POST['deliver_info']
            address = ShippingAddress.objects.get(id=shp_addr)
            cart_data = Cart.objects.filter(user = request.user)
            Order(customer=request.user,shipping_address=address,delivery_info=deliver_info).save()
            order = Order.objects.filter(customer=request.user).last()
            total = 0.0
            for data in cart_data:
                OrderItem(order=order, product=data.product, quantity=data.quantity).save()
                total = total + data.get_total_value
                data.delete()

            order.total = total
            order.save()

            order = OrderItem.objects.filter(order=order)
            print(order)
            return render(request, "thankyou.html", {'order':order, 'cart_count':0})
        else:
            return redirect('/')
    else:
        return redirect("/account/login.html")