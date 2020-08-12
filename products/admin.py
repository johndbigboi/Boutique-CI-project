from django.contrib import admin
from .models import Product, Category

# Register your models here.
"""
create two classes
product admin and category admin
Both of which will extend the built in model admin class.
"""


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'image',
    )

    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


'''
 sort the products by SKU using the ordering attribute.
Since it's possible to sort on multiple columns note that this does
have to be a tuple even though it's only one field.
To reverse it you can simply stick a minus in front of SKU.
'''

# we have to do is register our new classes alongside their respective models.
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
