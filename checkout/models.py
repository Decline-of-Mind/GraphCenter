from django.db import models
from django.conf import settings
import uuid

import os

from django_countries.fields import CountryField
from django.db.models import Sum
from services.models import Service

# Makes a dynamic path for the images provided by the user

def user_directory_path(instance, filename):
    return 'customer_images/user_{0}/{1}'.format(instance.user.id, filename)


class Order(models.Model):

    order_number = models.CharField(max_length=32, null=False, editable=False)
    date = models.DateTimeField(auto_now_add=True)
    STATUS = (
        ('requested', 'Requested'),
        ('pending', 'Pending'),
        ('finished', 'Finished')
    )

    # user = models.ForeignKey(settings.AUTH_USER_MODEL,
    #                          on_delete=models.CASCADE)
    full_name = models.CharField(max_length=40, null=False, blank=False)
    email = models.EmailField(max_length=100, null=False, blank=False)
    company_name = models.CharField(max_length=50, null=True, blank=True)
    phone_number = models.CharField(max_length=20, default='', null=False, blank=False)
    country = CountryField(multiple=False, blank_label='(select country)', null=False, blank=False)
    city = models.CharField(max_length=40, null=False, blank=False)
    zipcode = models.CharField(max_length=20, null=False, blank=False)
    street_address = models.CharField(max_length=80, null=False, blank=False)
    second_address = models.CharField(max_length=80, null=True, blank=True)
    region = models.CharField(max_length=80, null=True, blank=True)

    artwork = models.FileField(
        upload_to=user_directory_path, blank=True, null=True)
    description = models.TextField(max_length=250, blank=True, null=True)

    order_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    vat = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)

    original_cart = models.TextField(null=False, blank=False, default='')
    stripe_pid = models.CharField(max_length=254, null=False, blank=False, default='')
    status = models.CharField(
        choices=STATUS, default='requested', max_length=10)

    def _generate_order_number(self):
        '''
        Generates a random, unique order number with UUID
        '''
        return uuid.uuid4().hex.upper()

    def update_total(self):
        """
        Update grand total when line item is added,
        including vat taxes
        """
        self.order_total = self.lineitems.aggregate(Sum('lineitem_total'))['lineitem_total__sum'] or 0
        self.vat = self.order_total * settings.VATPERCENTAGE/100
        self.grand_total = self.order_total + self.vat
        self.save()

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the order number
        if it hasn't been set yet.
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
            super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


class OrderLineItem(models.Model):
    order = models.ForeignKey(Order,  null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems')
    service = models.ForeignKey(Service, null=False, blank=False, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1, null=False, blank=False)
    lineitem_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the order number
        if it hasn't been set yet.
        """
        self.lineitem_total = self.service.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f'Service: {self.service.name} on order {self.order.order_number}'



