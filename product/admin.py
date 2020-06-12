from django.contrib import admin

# Register your models here.
from .models import Product, Category,Brand, ProductImages



class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'price', 'condition', 'brand', 'posted_date', 'is_published', 'is_featured')
    list_display_links = ('owner', 'title')
    list_filter = ('owner', 'price')
    list_editable = ('condition', 'is_published', 'is_featured')
    search_fields = ('title', 'condition','brand')
    list_per_page = 25

admin.site.register(Product, ProductAdmin)

admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(ProductImages)