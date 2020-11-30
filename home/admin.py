from django.contrib import admin
from .models import Contact
# Register your models here.


class ContactAdmin(admin.ModelAdmin):
    model = Contact
    readonly_fields = ('user_email', 'subject', 'body', 'date')



admin.site.register(Contact, ContactAdmin)