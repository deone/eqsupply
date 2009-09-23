from django.contrib import admin
from quote_generator.models import *

admin.site.register(Manufacturer)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Quote)
admin.site.register(Price)
admin.site.register(QuoteItem)
