from django.db import models
from profiles.models import UserProfile


class Wishlist(models.Model):
    """ A model to link a wished product to the user """
    user = models.OneToOneField(UserProfile, null=False, blank=False, on_delete=models.CASCADE, related_name='wishlist')

    def __str__(self):
        return f'Wishlist ({self.user})'
