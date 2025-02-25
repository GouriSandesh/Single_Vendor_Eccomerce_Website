from os import path

from django.shortcuts import render, redirect, get_object_or_404

from ecoApp.forms import product_add_form
from ecoApp.models import Customers, Product, Order, OrderItem


def admin_dash(request):
    total_customers = Customers.objects.count()
    total_orders = Order.objects.count()
    total_products = Product.objects.count()
    print(total_customers,total_orders,total_products,"")
    context = {
        'total_customers' : total_customers,
        'total_orders' : total_orders,
        'total_products' : total_products,
    }
    return render(request,'admin_base.html',context)


def product_add(request):
    form = product_add_form()
    if request.method == 'POST':
        form = product_add_form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_view')
    return render(request, 'product.html', {'form':form})


def product_view(request):
    data = Product.objects.all()
    return render(request,'product_list.html',{'data':data})


def product_detail(request,pk):
    product_id = get_object_or_404(Product,pk=pk)
    return render(request,'product_Details.html',{'product_id':product_id})



def delete_product(request, id):
    data = Product.objects.get(id=id)
    data.delete()
    return redirect('product_view')


def update_product(request, id):
    data = Product.objects.get(id=id)
    form = product_add_form(instance=data)
    if request.method == 'POST':
        form = product_add_form(request.POST,request.FILES, instance=data)
        if form.is_valid():
            form.save()
            return redirect('product_view')
    return render(request,'update_product.html', {'form': form})


def custView(request):
    data = Customers.objects.all()
    return render(request, 'view_cust.html', {'data': data})


def cust_detail(request,pk):
    cust_id = get_object_or_404(Customers, pk=pk)
    context = {
        'cust_id' : cust_id
    }
    return render(request,'customer_details.html',{'cust_id':cust_id})




def admin_orders_view(request):
    orders = Order.objects.all().order_by('-order_date')  # Get all orders, latest first
    context = {
        'orders': orders,
    }
    return render(request, 'order_list.html', context)


def admin_order_detail_view(request, order_id):
    order = get_object_or_404(Order, order_id=order_id)
    order_items = OrderItem.objects.filter(order=order).select_related('product')  # Related items
    context = {
        'order': order,
        'order_items': order_items,
    }
    return render(request, 'order_detail.html', context)

