from django import template
from django.conf import settings

register = template.Library()

vat = settings.VATPERCENTAGE

@register.filter(name="calc_subtotal")
def calc_subtotal(price, quantity):
    return price * quantity

@register.filter(name="calc_vat")
def calc_vat(price, vat):
    return price * vat/100
