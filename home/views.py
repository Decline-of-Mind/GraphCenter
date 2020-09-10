from django.shortcuts import render

# Create your views here.


def index(request):
    """ view for the index page """
    return render(request, 'home/index.html')

