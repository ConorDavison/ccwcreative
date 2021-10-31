from django.shortcuts import render


def index(request):
    """
    a view to return index.html
    """
    return render(request, 'home/index.html')
