from django.shortcuts import render


def contactForm(request):
    return render(request, 'custom/custom_form.html')
