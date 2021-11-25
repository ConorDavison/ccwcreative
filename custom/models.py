from django.db import models


class Contact(models.Model):
    """
    A model for the contact form
    """

    name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.TextField()
    message = models.TextField()

    def __str__(self):
        return self.name
