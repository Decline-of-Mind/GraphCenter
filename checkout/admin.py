from django.contrib import admin
from .models import Order, OrderLineItem, BillingAddress


class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)

class BillingAddressAdminInline(admin.TabularInline):
    model = BillingAddress
    max_num = 1

    fields = ('company_name', 'country', 'region', 'city', 'street_address', 'zipcode', 'second_address')

    list_display = (
        'company_name',
        'street_address',
        'city',
        'region',
        'zipcode',
        'country',
        'second_address'
    )

class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline, BillingAddressAdminInline, )
    readonly_fields = ('order_number',
                       'date',
                       'vat_amount',
                       'order_total',
                       'grand_total')

    fields = ('order_number', 'date', 'user', 'vat_amount',
              'order_total', 'grand_total',)

    list_display = ('order_number', 'date', 'vat_amount',
                    'order_total', 'grand_total',)

    ordering = ('-date',)

admin.site.register(Order, OrderAdmin)



