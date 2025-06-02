from django.db import models
from shop_app.models import Product


class Order(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя*')
    phone = models.CharField(max_length=20, verbose_name='Номер телефона*')
    comment = models.CharField(max_length=300, blank=True, verbose_name='Комментарий')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    called = models.BooleanField(default=False, verbose_name='Звонок')

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Запросы на звонок'
        verbose_name_plural = 'Запросы на звонок'

    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete = models.CASCADE, verbose_name='Заказ')
    product = models.ForeignKey(Product, related_name='order_items', on_delete = models.PROTECT, verbose_name='Продукт')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    quantity = models.PositiveIntegerField(default=1, verbose_name='Количество')

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity
