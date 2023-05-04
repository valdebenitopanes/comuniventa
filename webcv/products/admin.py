from django.contrib import admin

# Register your models here.
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    fields = ('title','description','price','image','seller')
    list_display = ('__str__','slug','created_at','seller')
# para registrar productos
admin.site.register(Product,ProductAdmin)