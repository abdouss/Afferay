from django.contrib import admin

# Register your models here.
from .models import Product,Images


class PropertyImageInline(admin.StackedInline):
    model = Images
    extra = 2

class ProductAdmin(admin.ModelAdmin):

    prepopulated_fields = {'slug': ('Nom_Produit',)}
    inlines = [ PropertyImageInline, ]


class Imageadmin(admin.ModelAdmin):
	list_display =['product','image']
admin.site.register(Product,ProductAdmin)
admin.site.register(Images,Imageadmin)
