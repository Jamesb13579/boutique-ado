from django.contrib import admin
from .models import Product, Category

# Register your models here.

class Productadmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'image',
    )

    ordering =('sku',)

class Categoryadmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name'
    )

admin.site.register(Product, Productadmin)
admin.site.register(Category, Categoryadmin)