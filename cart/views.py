from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.


def view_cart(request):
    """ view for the shopping cart """

    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    quantity = 0
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        messages.error(
            request, 'Only one of the same service allowed')
        return redirect(redirect_url)
    else:
        cart[item_id] = quantity

    request.session['cart'] = cart
    return redirect('cart:view_cart')


    