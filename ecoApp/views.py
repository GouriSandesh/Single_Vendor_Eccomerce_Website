from django.contrib import messages, auth
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from ecoApp.forms import UserReg, Customer_reg
from ecoApp.models import Order


def homepage(request):
    return render(request,'home.html')


def login_page(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user= auth.authenticate(username=username, password=password)
        if user is not None and user.is_staff:
            login(request, user)
            return redirect('admin_dash')
        elif user is not None and user.is_customer:
            login(request, user)
            return redirect('user_home')
        else:
            messages.info(request, 'Invalid Credentials')
    return render(request, 'login3.html')


def user_home(request):
    return render(request, 'userHome.html')


def women(request):
    return render(request,'women.html')


def user_women(request):
    return render(request,'user_women.html')


def men(request):
    return render(request,'men.html')


def user_men(request):
    return render(request,'user_men.html')


def kids(request):
    return render(request,'kid.html')


def user_kids(request):
    return render(request,'user_kid.html')


def bags(request):
    return render(request, 'bags.html')


def user_bag(request):
    return render(request, 'user_bag.html')


def foot(request):
    return render(request, 'footwear.html')


def user_foot(request):
    return render(request, 'user_footwear.html')


def jewel(request):
    return render(request, 'Jewel.html')


def user_jewel(request):
    return render(request, 'user_jewel.html')


def admin(request):
    return render(request, 'admin2.html')

def custdash_view(request):
    current_user = request.user
    user_id = current_user.username
    print(user_id)
    context = {'user_id':user_id}
    return render(request, 'cust_base.html',context)


def cust_base(request):
    return render(request,'cust_base.html')


def signup(request):
    form1 = UserReg()
    form2 = Customer_reg()
    if request.method == 'POST':
        form1 = UserReg(request.POST)
        form2 = Customer_reg(request.POST)
        if form1.is_valid() and form2.is_valid():
            user = form1.save(commit=False)
            user.is_customer = True
            user.save()
            customer = form2.save(commit=False)
            customer.user = user
            customer.save()
            return redirect('login_page')
            messages.info(request, 'Successfully Registered')
    return render(request, 'register_new.html', {'form1': form1, 'form2': form2})



def signout(request):
    logout(request)
    messages.success(request, 'Logged Out Successfully')
    return redirect('homepage')



@login_required()
def orders_view(request):
    orders = Order.objects.filter(user=request.user)
    context = {
        'orders': orders,
        'title': 'My Orders Dashboard',
    }
    return render(request, 'myOrder.html', context)



def delete_order(request):
    data = Order.objects.get(id=id)
    data.delete()
    return redirect('orders_view')


def delete_account(request):
    request.user.delete()
    messages.info(request, 'Account deleted Successfully')
    return redirect('homepage')
