from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.users.models import User
from apps.catalog.models import Product

class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', _('Ожидание')),
        ('processing', _('В обработке')),
        ('shipped', _('Отправлено')),
        ('delivered', _('Доставлено')),
        ('canceled', _('Отменено')),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_("Пользователь"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Дата создания"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Дата обновления"))
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending', verbose_name=_("Статус"))
    total_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_("Общая сумма"))
    shipping_address = models.TextField(verbose_name=_("Адрес доставки"))
    billing_address = models.TextField(verbose_name=_("Адрес оплаты"))

    class Meta:
        verbose_name = _("Заказ")
        verbose_name_plural = _("Заказы")

    def __str__(self):
        return f"Order #{self.id} by {self.user.username}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE, verbose_name=_("Заказ"))
    product = models.ForeignKey(Product, on_delete=models.PROTECT, verbose_name=_("Продукт"))
    quantity = models.PositiveIntegerField(verbose_name=_("Количество"))
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_("Цена"))

    class Meta:
        verbose_name = _("Позиция заказа")
        verbose_name_plural = _("Позиции заказа")

    def __str__(self):
        return f"{self.product.name} ({self.quantity})"
