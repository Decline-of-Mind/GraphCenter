from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline, )
    readonly_fields = ('order_number',
                       'date',
                       'vat_amount',
                       'order_total',
                       'grand_total',
                       )

    fields = ('order_number', 'date', 'user', 'vat_amount',
              'order_total', 'grand_total',
              'email'
              'full_name',
              'company_name',
              'phone_number',
              'street_address',
              'city',
              'region',
              'zipcode',
              'country',
              'second_address',)

    list_display = ('order_number', 'date', 'full_name', 'vat_amount',
                    'order_total', 'grand_total', 'email',
                    )

    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)


