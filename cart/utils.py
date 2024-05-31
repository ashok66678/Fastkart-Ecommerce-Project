from cart.models import Cart


def cartCount(request):

    cart_count = 0
    cart_data = Cart.objects.filter(user=request.user)
    total = 0.0
    for cart in cart_data:
        cart_count = cart_count + cart.quantity
        total = total + cart.get_total_value
    
    return {"cart_data":cart_data,"cart_count":cart_count, "total_cart_value":total}
    