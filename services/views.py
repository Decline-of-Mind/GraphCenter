from django.shortcuts import render
from .models import Service, Category

# Create your views here.


def services(request):
    """ view for the services page """

    services = Service.objects.all()
    category = None

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            services = services.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

    context = {
        'services': services,
        'current_categories': categories,
    }

    return render(request, 'services/services.html', context)
