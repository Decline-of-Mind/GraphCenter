from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .models import Order, OrderLineItem
from .forms import OrderForm

def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "Cart is empty")
        return redirect(reverse('services'))
    orderform = OrderForm()
    # orderlineform = OrderLineForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': orderform,
    }

    return render(request, template, context)

