from django.contrib import admin
from .models import Vendor, Product, ProductCategory

admin.site.register(Vendor)
admin.site.register(Product)
admin.site.register(ProductCategory)
