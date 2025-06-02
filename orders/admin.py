from django.contrib import admin
from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'phone', 'comment', 'created',
                    'called']
    list_filter = ['called', 'created']
    inlines = [OrderItemInline]
    readonly_fields = ('name', 'created',)

admin.site.register(Order, OrderAdmin)
