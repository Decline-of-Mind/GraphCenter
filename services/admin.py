from django.contrib import admin
from .models import Service, Category

# Register your models here.


class ServiceAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'category',
        'price',
        'image',
    )

    ordering = ('category',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'friendly_name'
    )


admin.site.register(Category, CategoryAdmin)

admin.site.register(Service, ServiceAdmin)

