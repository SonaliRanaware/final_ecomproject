from django.contrib import admin
from .models import product,cart,orders1
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
      list_display=['id','name','price','pdetails','cat','is_active']
      list_filter=['cat','is_active']
class cartAdmin(admin.ModelAdmin):
      list_display=['id','uid','pid']
class OrderAdmin(admin.ModelAdmin):
      list_display=['id','order_id','uid','pid']      
admin.site.register(cart,cartAdmin)            
admin.site.register(product,ProductAdmin)    
admin.site.register(orders1,OrderAdmin)        