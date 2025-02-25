from django.contrib import admin

from ecoApp import models
from ecoApp.models import OrderItem, Payment, Order

# Register your models here.
admin.site.register(models.Customers)
admin.site.register(models.Product)
admin.site.register(models.Order)
admin.site.register(models.Cart)
admin.site.register(models.CartItem)


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    readonly_fields = ('product', 'quantity', 'unit_price', 'total_price')
    can_delete = False
    extra = 0

class PaymentInline(admin.TabularInline):
    model = Payment
    readonly_fields = ('payment_method', 'transaction_id', 'payment_date', 'amount', 'status', 'remarks')
    can_delete = False
    extra = 0

class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_id', 'user', 'order_date', 'total_price')
    list_filter = ('order_date', 'user')
    search_fields = ('order_id', 'user__username')
    readonly_fields = ('order_id', 'order_date', 'total_price')
    inlines = [OrderItemInline, PaymentInline]

    def has_add_permission(self, request):
        # Optional: Disable adding orders directly from admin
        return False

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('transaction_id', 'user', 'order', 'payment_method', 'amount', 'status', 'payment_date')
    list_filter = ('payment_date', 'payment_method', 'status')
    search_fields = ('transaction_id', 'user__username', 'order__order_id')
    readonly_fields = ('transaction_id', 'payment_date', 'order', 'user')

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'product', 'quantity', 'unit_price', 'total_price')
    search_fields = ('order__order_id', 'product__product_name')
