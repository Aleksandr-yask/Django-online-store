from django.db import models
from products.models import Product, ProductImage
from django.db.models.signals import post_save
# Create your models here.

class Status(models.Model):
    status_name = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return "%s" % self.status_name

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'

    def save(self, *args, **kwargs):
        super(Status, self).save(*args, **kwargs)


        # ======================================================================================================


class Order(models.Model):
    customer_name = models.CharField(max_length=100)
    customer_email = models.EmailField()
    customer_phone = models.CharField(max_length=20, blank=True, default=None)
    customer_adress = models.CharField(max_length=200, blank=True, default=None)
    comments = models.TextField(blank=True, null=True, default=None)
    # img = models.CharField(max_length=300, blank=True, default=None, null=True)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return "Заказ %s, Статус: %s" % (self.id, self.customer_name)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def save(self, *args, **kwargs):
        super(Order, self).save(*args, **kwargs)


        # ======================================================================================================

class ProductInOrder(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    # img = models.CharField(max_length=300, blank=True, default=None, null=True)
    is_active = models.BooleanField(default=True)
    nmb = models.IntegerField(default=1)
    price_per_item = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    # ======================================================================================================


    def __str__(self):
        return "%s" % self.product.product_name

    class Meta:
        verbose_name = 'Товар в заказе'
        verbose_name_plural = 'Товары в заказе'

    def save(self, *args, **kwargs):
        price_per_item = self.product.product_price
        self.price_per_item = price_per_item
        self.total_price = self.nmb * self.price_per_item

        super(ProductInOrder, self).save(*args, **kwargs)

# ======================================================================================================

def product_in_order_post_save(sender, instance, created, **kwargs):
    order = instance.order
    all_products_in_order = ProductInOrder.objects.filter(order=order, is_active=True)

    order_total_price = 0
    for item in all_products_in_order:
        order_total_price += item.total_price

    instance.order.total_price = order_total_price
    instance.order.save(force_update=True)

post_save.connect(product_in_order_post_save, sender = ProductInOrder)

# ======================================================================================================

class ProductInBasket(models.Model):
    session_key = models.CharField(max_length=128, null=False, default=None)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    product_image = models.ForeignKey(ProductImage, on_delete=models.CASCADE, null=True)
    nmb = models.IntegerField(default=1)
    price_per_item = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    img = models.CharField(max_length=300, blank=True, default=None, null=True)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)



    def __str__(self):
        return "%s" % self.product.product_name

    class Meta:
        verbose_name = 'Товар в корзине'
        verbose_name_plural = 'Товары в корзине'

    def save(self, *args, **kwargs):
        price_per_item = self.product.product_price
        self.price_per_item = price_per_item
        self.total_price = int(self.nmb) * self.price_per_item

        super(ProductInBasket, self).save(*args, **kwargs)