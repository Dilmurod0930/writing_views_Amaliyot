from django.contrib import admin
from  .models  import Product , Category
# Register your models here.

# admin.site.register(Product)
admin.site.register(Category)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'discount', 'category']
    list_filter = ['category',]
    search_fields = ['name']
