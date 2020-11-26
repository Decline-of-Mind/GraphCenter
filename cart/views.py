from django.shortcuts import render, redirect, get_object_or_404, reverse, HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist

from services.models import Service

# Create your views here.


def view_cart(request):
    """ view for the shopping cart """

    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """ Add a product to the shopping cart"""

    service = get_object_or_404(Service, pk=item_id)
    quantity = int(request.POST.get('quantity'))

    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    # Checks if the item is already in the bag, returns error if it does.
    if item_id in list(cart.keys()):
        messages.error(
            request, 'Only one of the same service allowed')
        return redirect(redirect_url)
    else:
        cart[item_id] = quantity
        messages.success(request, f'Added {service.name} to your shopping bag')
        print(f'Added {service.name} to your shopping cart')

    request.session['cart'] = cart
    return redirect(redirect_url)


def delete_from_cart(request, item_id):

    '''Removes service from the cart'''
    try:
        cart = request.session.get('cart', {})
        service = get_object_or_404(Service, pk=item_id)

        if item_id in list(cart.keys()):
            cart.pop(item_id)
            messages.success(request, f'{service.name} has been removed from the cart')

        request.session['cart'] = cart
        return redirect(reverse('view_cart'))

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
