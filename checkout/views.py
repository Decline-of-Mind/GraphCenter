from django.shortcuts import render, redirect, reverse
from django.contrib import messages

def checkout(request):
    cart = request.session.get('bag', {})
    if not cart:
        messages.error(request, "Cart is empty")
        return redirect(reverse('services'))

    billingform = BillingForm()
    orderlineform = OrderLineForm()
    template = 'checkout/checkout.html'
    context = {
        'billing_form': billingform,
        'orderlineform': orderlineform,
    }

    return render(request, template, context)

