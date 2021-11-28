from django.shortcuts import (
    render, redirect, get_list_or_404, get_object_or_404)

from .models import Product, UserProfile, Wishlist, WishlistItem

from django.contrib.auth.decorators import login_required

from django.utils import timezone

from django.contrib import messages


@login_required
def wishlist(request):
    """ A view to return the Wishlist """
    items = []
    user = get_object_or_404(UserProfile, user=request.user)
    wishlist = Wishlist.objects.get_or_create(user=user)
    wishlist_user = wishlist[0]
    test = WishlistItem.objects.filter(wishlist=wishlist_user).exists()

    if test:
        user_wishlist = get_list_or_404(WishlistItem, wishlist=wishlist_user)
        for obj in user_wishlist:
            product = get_object_or_404(Product, name=obj)
            items.append(product)
        context = {
            'wishlist': True,
            'products': items
        }
        return render(request, 'wishlist/wishlist.html', context)

    else:
        context = {
            'wishlist': False,
        }
        return render(request, 'wishlist/wishlist.html', context)


@login_required
def add_to_wishlist(request, product_id):
    """ A view to add a item in the Wishlist """
    redirect_url = request.POST.get('redirect_url')

    user = get_object_or_404(UserProfile, user=request.user)
    wishlist = Wishlist.objects.get_or_create(user=user)
    wishlist_user = wishlist[0]

    product = Product.objects.get(pk=product_id)
    if request.POST:
        test = WishlistItem.objects.filter(
            wishlist=wishlist_user, product=product).exists()
        if test:
            messages.error(request, "Product already in your wishlist")
            return redirect(redirect_url)

        else:
            added_item = WishlistItem(
                wishlist=wishlist_user,
                product=product, date_added=timezone.now())
            added_item.save()
            messages.success(request, "Product added to your wishlist")
            return redirect(redirect_url)
    else:
        messages.error(request, "Click 'Add to wishlist' to add a item ")
        return render(request, 'home/index.html')


@login_required
def delete_from_wishlist(request, product_id):
    """ A view to delete a item in the wishlist"""

    redirect_url = request.POST.get('redirect_url')

    user = get_object_or_404(UserProfile, user=request.user)
    wishlist = Wishlist.objects.get_or_create(user=user)
    wishlist_user = wishlist[0]
    if request.POST:
        product = Product.objects.get(pk=product_id)

    # look for product in the user's wishlistItem - returns true if it exists
        test = WishlistItem.objects.filter(product=product).exists()

        if test:
            product = WishlistItem.objects.get(product=product)
            product.delete()
            messages.success(request, "Product removed from wishlist")
            return redirect(redirect_url)

        if test is None:
            messages.error(
                request,
                "You can not delete a item that is not in your wishlist")
            return redirect(redirect_url)
    else:
        messages.error(request, 'Item can only be deleted from your wishlist')
        return render(request, 'home/index.html')
