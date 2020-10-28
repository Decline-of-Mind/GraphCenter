from django.shortcuts import render
from .models import Service

# Create your views here.


def services(request):
    """ view for the services page """

    services = Service.objects.all()

    context = {
        'services': services,
    }

    return render(request, 'services/services.html', context)
