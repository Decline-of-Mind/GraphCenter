from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from services.models import Service


def cart_contents(request):

    cart_items = []
    total = 0
    service_count = 0
    cart = request.session.get('cart', {})

    for item_id, quantity in cart.items():
        service = get_object_or_404(Service, pk=item_id)
        total += quantity * service.price
        vat = total * Decimal(settings.VATPERCENTAGE/100)
        service_count += quantity
        cart_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'service': service,
        })

    grand_total = total + vat

    context = {
        'cart_items': cart_items,
        'total': total,
        'vat': vat,
        'service_count': service_count,
        'grand_total': grand_total,
    }

    return context
