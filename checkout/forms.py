from django import forms
from .models import Order, BillingAddress, OrderLineItem


class BillingForm(forms.ModelForm):
    class Meta:
        model = BillingAddress
        fields = ('company_name', 'phone_number', 'country', 'region',
                  'city', 'street_address', 'zipcode', 'second_address')

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on the first field
        """
        super().__init__(self, *args, **kwargs)
        placeholders = {
                'company_name': 'Company Name',
                'phone_number': 'Phone Number',
                'country': 'Country',
                'region': 'Province',
                'city': 'City',
                'street_address': 'Street Address',
                'zip_code': 'Postal Code',
                'second_street': '2nd Street Address',
            }

        self.fields['phone_number'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False


class OrderLineForm(forms.ModelForm):
    class Meta:
        model = OrderLineItem
        fields = ('artwork', 'description',)

        def __init__(self, *args, **kwargs):
            """
            Add placeholders and classes, remove auto-generated
            labels and set autofocus on the first field
            """
            super().__init__(*args, **kwargs)
            placeholders = {
                'artwork': 'Artwork',
                'description': 'Description'
            }

