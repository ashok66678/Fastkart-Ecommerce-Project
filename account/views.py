from django.shortcuts import render, redirect
from django.contrib import auth
from .models import ShippingAddress
from django.http import HttpResponse
# from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.models import User, Group
from .forms import RegisterForm
from account.models import User as MyUser
from django.contrib.auth.hashers import make_password
from cart.utils import cartCount
from order.models import Order, OrderItem





# Create your views here.

def login(request):

    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == 'POST':
            email = request.POST['email']
            password = request.POST['password']
            user = auth.authenticate(email=email, password=password)
            if user is not None:
                auth.login(request, user)  ## to start the login session
                try:
                    return redirect(request.GET['next']) ## next means?
                except:
                    return redirect('/') 
            else:
                error = "Username or Password is incorrect"
                return render(request, 'login.html', {"error": error, 'cart_count':'0'})
        return render(request, 'login.html',{'cart_count':'0'})



def logout(request):
    auth.logout(request)
    return redirect('/')


def register(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        form = {}
        if request.method == 'POST':
            email = request.POST['email']
            full_name = request.POST['full_name']
            password = request.POST['pass1']
            password2 = request.POST['pass2']
            form_data = {"email": email, 'full_name': full_name, "password": password, "password2": password2, }
            form = RegisterForm(form_data)
            if form.is_valid():
                user = MyUser(email=email, password=make_password(password), full_name=full_name)
                user.save()
                user = auth.authenticate(email=email, password=password)
                
                if user is not None:
                    auth.login(request, user)
                    return redirect('/')
                return redirect('register')
            else:
                return render(request, 'register.html', {"form": form})
        return render(request, 'register.html', {"form": form})
    

def addAddress(request):
    if request.user.is_authenticated:
        cart_data = cartCount(request)
        if request.method == "POST":
            name = request.POST['name']
            phone = request.POST['telephone']
            address = request.POST['address']
            city = request.POST['city']
            state = request.POST['state']
            zip = request.POST['zip']

            if len(name) > 2 and len(phone) == 10 and len(address) > 5 and len(city) >= 3 and len(zip) == 6 :
                ShippingAddress(customer = request.user,name = name, phone_no = phone, 
                                address= address, city = city, 
                                 state = state, zipcode = zip).save()

                return redirect('checkout') 
            else:
                return render(request, "add_address.html", {'error':'Please fill all the details carefully',
                                                            'cart_count':cart_data['cart_count'] })
        else:

            return render(request, "add_address.html",{'cart_count':cart_data['cart_count']})
    else:
        return redirect('/account/login/')
    

def dashboard(request):
    if request.user.is_authenticated:
        data = []
        orders = Order.objects.filter(customer = request.user).order_by("-id")    #ADDED
        user = MyUser.objects.get(email=request.user)
        cart_data = cartCount(request)
            
        data = OrderItem.objects.filter(order__in=[order.id for order in orders])
        # for order in orders:
        #     data.append(OrderItem.objects.filter(order = order))

        addresses = ShippingAddress.objects.filter(customer=request.user)

        # print("\n\nOrder data: ",data," \n\nOrders: ",orders, "\n\nUSer: ",user,"\n\nAddressses: ",addresses)

        context = {"OrderItems":data, 'orders':orders,'user':user, "cart_count":cart_data['cart_count'],'addresses':addresses}
        return render(request, "dashboard.html", context)

    else:
        return redirect("/account/login.html")
    
    
def addressToDelete(request,address_id):    
    if request.user.is_authenticated:
        cust_address = ShippingAddress.objects.get(id= address_id, customer=request.user)
        cust_address.is_active = False
        cust_address.save()
        return redirect(request.META.get('HTTP_REFERER'))
        
    else: 
        return redirect(request.META.get('HTTP_REFERER'))