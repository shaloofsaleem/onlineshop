from msilib.schema import Class
from django.contrib import admin
from.models import *

# Register your models here.

class Categoryadmin(admin.ModelAdmin):
  prepopulated_fields={'slug':('name',)}
admin.site.register(Category,Categoryadmin)
admin.site.register(Sub_Category)

admin.site.register(Brand)

class ProductAdmin(admin.ModelAdmin):
  prepopulated_fields={'slug':('name',)}
admin.site.register(Product,ProductAdmin)  


admin.site.register(Contact_us)


admin.site.register(order)