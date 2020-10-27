from django.shortcuts import render

# Create your views here.


def services(request):
    """ view for the services page """
    return render(request, 'services/services.html')
