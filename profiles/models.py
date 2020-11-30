from django.db import models
from django_countries.fields import CountryField
from django.contrib.auth.models import User

from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver




class UserProfile(models.Model):
    """"
    Model to store billing information and order history
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_company_name = models.CharField(max_length=50, null=True, blank=True)
    default_phone_number = models.CharField(max_length=20, null=True, blank=True)
    default_country = CountryField(multiple=False, blank_label='(select country)', null=False, blank=True)
    default_city = models.CharField(max_length=40, null=True, blank=True)
    default_zipcode = models.CharField(max_length=20, null=True, blank=True)
    default_street_address = models.CharField(max_length=80, null=True, blank=True)
    default_second_address = models.CharField(max_length=80, null=True, blank=True)
    default_region = models.CharField(max_length=80, null=True, blank=True)

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """ 
    Create or adjust the user profile
    """
    if created:
        UserProfile.objects.create(user=instance)
    # Updating just saves
    instance.userprofile.save()