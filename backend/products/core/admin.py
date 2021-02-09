from django.contrib import admin

from products.core.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'price')
    list_display_links = ('name', 'id')
    search_fields = ('id', 'name')
