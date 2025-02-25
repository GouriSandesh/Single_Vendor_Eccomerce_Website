
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from ecoApp.models import Product, Wishlist, WishlistItem


# Add a product to the wishlist
@login_required()
def add_to_wishlist(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    wishlist, created = Wishlist.objects.get_or_create(user=request.user)
    wishlist_item, created = WishlistItem.objects.get_or_create(wishlist=wishlist, product=product)

    if created:
        wishlist_item.save()

    return redirect('wishlist_detail')

# View the wishlist
@login_required()
def wishlist_detail(request):
    wishlist = Wishlist.objects.get(user=request.user)
    return render(request, 'myWishlist.html', {'wishlist': wishlist})

# Remove an item from the wishlist
@login_required(login_url='login_page')
def remove_from_wishlist(request, product_id):
    wishlist = Wishlist.objects.get(user=request.user)
    product = get_object_or_404(Product, id=product_id)
    wishlist_item = get_object_or_404(WishlistItem, wishlist=wishlist, product=product)
    wishlist_item.delete()
    return redirect('wishlist_detail')