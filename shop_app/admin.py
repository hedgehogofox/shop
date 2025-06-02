from django.contrib import admin
from .models import Product, Bathroom_accessories, Bath, Plumbing, Sink, Furniture, Sanfayance, Faucet, Towel_rail


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'art', 'price', 'stock', 'available']
    list_filter = ['available', 'created', 'updated', 'maker']
    list_editable = ['price', 'stock', 'available']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Product, ProductAdmin)

class Bathroom_accessoriesAdmin(admin.ModelAdmin):
    list_display = ['product', 'size']
    list_editable = ['size']
admin.site.register(Bathroom_accessories, Bathroom_accessoriesAdmin)

class BathAdmin(admin.ModelAdmin):
    list_display = ['product', 'coating', 'hydromassage', 'form']
    list_editable = ['coating', 'hydromassage', 'form']
admin.site.register(Bath, BathAdmin)

class PlumbingAdmin(admin.ModelAdmin):
    list_display = ['product', 'size']
    list_editable = ['size']
admin.site.register(Plumbing, PlumbingAdmin)

class SinkAdmin(admin.ModelAdmin):
    list_display = ['product', 'number_of_bowls', 'shredder', 'form']
    list_editable = ['number_of_bowls', 'shredder', 'form']
admin.site.register(Sink, SinkAdmin)

class FurnitureAdmin(admin.ModelAdmin):
    list_display = ['product', 'mounting', 'backlight']
    list_editable = ['mounting', 'backlight']
admin.site.register(Furniture, FurnitureAdmin)

class SanfayanceAdmin(admin.ModelAdmin):
    list_display = ['product', 'drain_mode', 'mounting', 'form']
    list_editable = ['drain_mode', 'mounting', 'form']
admin.site.register(Sanfayance, SanfayanceAdmin)

class FaucetAdmin(admin.ModelAdmin):
    list_display = ['product', 'size', 'spout', 'appointment']
    list_editable = ['size', 'spout', 'appointment']
admin.site.register(Faucet, FaucetAdmin)

class Towel_railAdmin(admin.ModelAdmin):
    list_display = ['product', 'connection', 'type', 'form']
    list_editable = ['connection', 'type', 'form']
admin.site.register(Towel_rail, Towel_railAdmin)
