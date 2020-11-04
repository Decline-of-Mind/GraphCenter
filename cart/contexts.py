from django.conf import settings


def cart_contents(request):

    bag_items = []
    total = 0
    service_count = 0


    grand_total = total

    context = {
        'bag_items': bag_items,
        'total': total,
        'service_count': service_count,
        'grand_total': grand_total,
    }

    return context
