from django.contrib import admin
from .models import *

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', "title", 'description')
    list_display_links = ('id', "title", 'description')
    search_fields = ("title", 'description')
    ordering = ["id"]

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'price', 'amount']
    list_display_links = ['id', 'title', 'price', 'amount']
    search_fields = ["id", 'title']
    ordering = ['price', 'amount']
    list_filter = ['active', 'price']
    readonly_fields = ['img_preview']


@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    list_display_links = ['id', 'title']
    search_fields = ["title"]
    ordering = ['id']
    readonly_fields = ['img_preview']

admin.site.register(Images)