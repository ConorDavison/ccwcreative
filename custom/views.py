from django.shortcuts import render
from django.contrib import messages
from .models import Contact


def contactForm(request):
    """
    A View for the contact form
    """

    if request.method == "POST":

        contact = Contact()
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        contact.name = name
        contact.email = email
        contact.subject = subject
        contact.message = message
        contact.save()
        messages.success(request, 'Message recieved!')
    return render(request, 'custom/custom_form.html')
