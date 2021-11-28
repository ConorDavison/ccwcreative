from django.db import models
from profiles.models import UserProfile
from products.models import Product


class Wishlist(models.Model):
    """ A model to link a wished product to the user """
    user = models.OneToOneField(
        UserProfile,
        on_delete=models.CASCADE,
        null=False, blank=False,
        related_name='wishlist')

    def __str__(self):
        return f'Wishlist ({self.user})'


class WishlistItem(models.Model):
    """A many to many model to wishlist products"""
    wishlist = models.ForeignKey(
        Wishlist,
        on_delete=models.CASCADE,
        null=False, blank=False,
        related_name='wishlist_items')
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        null=False, blank=False,
        related_name='wishlist_products')
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product.name
