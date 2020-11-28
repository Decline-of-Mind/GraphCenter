from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .models import Order, OrderLineItem
from .forms import OrderForm, OrderLineForm

def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "Cart is empty")
        return redirect(reverse('services'))
    orderform = OrderForm()
    orderlineform = OrderLineForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': orderform,
        'orderline_form': orderlineform,
        'stripe_public_key': 'pk_test_51HMCRhDhaBLdkalb5zedZXoFDGJM93OZWaqyMGqWJypgmtSmfCcBGTJQ0Z69XzMeNXSGgsJjnOAo2dlP84zA35wF00FBWY1o2Y',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)

