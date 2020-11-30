from django import forms

from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user',)


    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on the first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
                'default_company_name': 'Company Name',
                'default_phone_number': 'Phone Number',
                'default_country': 'Country',
                'default_region': 'County, State or Province',
                'default_city': 'City',
                'default_street_address': 'Street Address',
                'default_zipcode': 'Postal Code',
                'default_second_address': '2nd Street Address',
            }

        self.fields['default_phone_number'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'default_country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'border-black rounded-0 profile-form-input'
            self.fields[field].label = False


