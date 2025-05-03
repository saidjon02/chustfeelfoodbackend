# api/admin.py
from django.contrib import admin
from .models import Product, Order

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'img')
    list_editable = ('price', 'img')
    search_fields = ('name',)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone', 'total', 'created_at')
    list_filter = ('created_at',)
    readonly_fields = ('created_at',)
