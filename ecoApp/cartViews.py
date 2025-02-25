from itertools import count


from _decimal import Decimal
from django.contrib import auth, messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, request
from django.shortcuts import get_object_or_404, redirect, render


from ecoApp.models import Cart, CartItem, Product



@login_required
def add_to_cart(request, product_id):
   product = get_object_or_404(Product, id=product_id)
   cart, created = Cart.objects.get_or_create(user=request.user)
   cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)




   if not created:
       cart_item.quantity += 1
   cart_item.save()




   return redirect('cart_detail')


@login_required
def cart_detail(request):
   cart = Cart.objects.get(user=request.user)
   item_count = cart.items.count()
   total_price = 0
   sum=0
   for item in cart.items.all():
       total_price += int(item.product.price) * item.quantity  # Assuming price is stored as a string
       sum += int(total_price) + 3
   return render(request, 'cart.html', {'cart': cart, 'total_price': total_price, 'item_count':item_count,'sum':sum })






def remove_from_cart(request, product_id):
    cart = Cart.objects.get(user=request.user)
    product = get_object_or_404(Product, id=product_id)
    cart_item = get_object_or_404(CartItem, cart=cart, product=product)
    cart_item.delete()
    return redirect('cart_detail')
#
# # # Increase Quantity View
def increase_quantity(request, product_id):
    # Handle authenticated and unauthenticated users
    if request.user.is_authenticated:
        # Fetch the cart for the logged-in user
        cart = Cart.objects.get(user=request.user)
    else:
        # Fetch the cart using the session for guest users
        cart_id = request.session.get('cart_id')
        if not cart_id:
            # If no cart exists in the session, redirect to the cart detail page
            return redirect('cart_detail')  # Or handle the error appropriately
        else:
            # Retrieve the existing guest cart
            cart = Cart.objects.get(id=cart_id)


    # Retrieve the product and the corresponding cart item
    product = get_object_or_404(Product, id=product_id)
    cart_item = get_object_or_404(CartItem, cart=cart, product=product)


    # Increase the quantity of the item
    cart_item.quantity += 1
    cart_item.save()


    # Redirect back to the cart detail page
    if request.user.is_authenticated:
        return redirect('cart_detail')  # Redirect authenticated users to their user cart page
    # Redirect unauthenticated users to the general cart detail page






#  # Decrease Quantity View
def decrease_quantity(request, product_id):
    # Handle authenticated and unauthenticated users
    if request.user.is_authenticated:
        # Fetch the cart for the logged-in user
        cart = Cart.objects.get(user=request.user)
    else:
        # Fetch the cart using the session for guest users
        cart_id = request.session.get('cart_id')
        if not cart_id:
            # If no cart exists, redirect to the cart detail page
            return redirect('cart_detail')  # Or show an error message
        else:
            # Retrieve the existing guest cart
            cart = Cart.objects.get(id=cart_id)


    # Retrieve the product and the corresponding cart item
    product = get_object_or_404(Product, id=product_id)
    cart_item = get_object_or_404(CartItem, cart=cart, product=product)


    # Decrease the quantity or remove the item if quantity is 1
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()  # Remove the item if the quantity reaches 0


    # Redirect back to the cart detail page
    if request.user.is_authenticated:
        return redirect('cart_detail')  # Redirect authenticated users to their user cart page
