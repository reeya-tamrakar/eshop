from django.contrib import admin

from .models import ProductCategory
from .models import Product
from .models import ContactResponse

admin.site.register(ProductCategory)
admin.site.register(Product)
admin.site.register(ContactResponse)