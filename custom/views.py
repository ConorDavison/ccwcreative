from django.shortcuts import render
from .models import contact
from django.http import HttpResponse
from django.contrib import messages


def contactForm(request):
    if request.method == "POST":

        contact = contact()
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
