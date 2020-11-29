from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('full_name', 'company_name', 'email', 'phone_number',
                  'country', 'region', 'city', 'street_address', 'zipcode',
                  'second_address', 'artwork', 'description', 'status')

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on the first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
                'full_name': 'Full Name',
                'email': 'Email Address',
                'company_name': 'Company Name',
                'phone_number': 'Phone Number',
                'country': 'Country',
                'region': 'County, State or Province',
                'city': 'City',
                'street_address': 'Street Address',
                'zipcode': 'Postal Code',
                'second_address': '2nd Street Address',
                'artwork': 'Your Artwork',
                'description': 'Max 250 characters',
                'status': 'status',
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


