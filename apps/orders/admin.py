from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from apps.orders.models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'created_at', 'updated_at', 'status', 'total_price')
    list_filter = ('status', 'created_at', 'updated_at')
    search_fields = ('user__username', 'user__email')
    inlines = [OrderItemInline]

    def total_price(self, obj):
        return sum(item.price * item.quantity for item in obj.items.all())

    total_price.short_description = _("Общая сумма")


admin.site.register(OrderItem)
