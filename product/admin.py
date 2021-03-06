from django.contrib import admin

# Register your models here.

from . models import Category, Images, Product
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'parent', 'status']
    list_filter = ['status']

class ProductImageInline(admin.TabularInline):
    model = Images
    extra = 1


class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'status']
    list_filter = ['category', 'discount']  
    readonly_fields = ('image_tag',)  
    inlines = [ProductImageInline]

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Images)