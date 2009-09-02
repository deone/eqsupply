from django.contrib import admin
from quote_generator.models import Manufacturer, Category, Product

admin.site.register(Manufacturer)
admin.site.register(Category)
admin.site.register(Product)
