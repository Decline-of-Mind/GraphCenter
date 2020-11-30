from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Contact
from .forms import ContactForm
from django.conf import settings


def index(request):
    """ view for the index page """
    return render(request, 'home/index.html')


def contact(request):
    contact = Contact
    form = ContactForm()

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully Contacted GraphCenter')
            return redirect('home')
        else:
            messages.error(request, 'Something went wrong with'
                                    'submitting your contact form.'
                                    'Please try again.')

    template = 'home/contact.html/'
    context = {
        'form': form,
        'contact': contact,
    }

    return render(request, template, context)

