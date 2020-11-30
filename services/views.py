from django.shortcuts import render, get_object_or_404
from .models import Service, Category

from .forms import ServiceForm


def services(request):
    """ view for the services page """

    services = Service.objects.all()
    categories = None

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


def service_detail(request, service_id):

    """ view to show details of a service """

    service = get_object_or_404(Service, pk=service_id)
    context = {
        'service': service,
    }

    return render(request, 'services/service_details.html', context)


def add_service(request):
    """ Add a Service to the store"""
    if request.method == "POST":
        form = ServiceForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully Added Service!')
            return redirect(reverse('add_service'))
        else:
            messages.error(request, 'Failed to add Service. Please ensure the form is valid.')

    else:
        form = ServiceForm()
    
    
    template = 'services/add_service.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
