from django.db import models
# Create your models here.

class ProductCategory(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = 'Категория товара'
        verbose_name_plural = 'Категории товаров'

# ======================================================================================================

class ProductSex(models.Model):
    name_sex = models.CharField(max_length=64, blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return "%s" % self.name_sex

    class Meta:
        verbose_name = 'Пол'
        verbose_name_plural = 'Полы'

# ======================================================================================================

class ProductClass(models.Model):
    name_class = models.CharField(max_length=64, blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return "%s" % self.name_class

    class Meta:
        verbose_name = 'Class'
        verbose_name_plural = 'Classes'


# class ProductColors(models.Model):
#     name_color = models.CharField(max_length=64, blank=True, null=True)
#     is_active = models.BooleanField(default=True)
#
#     def __str__(self):
#         return "%s" % self.name_color
#
#     class Meta:
#         verbose_name = 'Цвет'
#         verbose_name_plural = 'Цвета'


class Product(models.Model):
    product_name = models.CharField(max_length=100, blank=True, null=False, default=None)
    product_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, null=False)
    product_description = models.TextField(blank=True, null=True, default=None)
    product_category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, default=1, null=False)
    product_class = models.ForeignKey(ProductClass, on_delete=models.CASCADE, default=1, null=False)
    sex = models.ForeignKey(ProductSex, on_delete=models.CASCADE, default=1, null=False)
    product_number = models.CharField(max_length=10, blank=True, default='JH-172', null=False)
    paramount = '1'
    secondary = '2'
    YEAR_IN_SCHOOL_CHOICES = (
        (secondary, 'Secondary'),
        (paramount, 'Paramount')
    )
    importance = models.CharField(
        max_length=2,
        choices=YEAR_IN_SCHOOL_CHOICES,
        default=1
    )
    is_best_seller = models.BooleanField(default=False)
    is_top_rate = models.BooleanField(default=False)
    is_new = models.BooleanField(default=False)
    is_sale = models.BooleanField(default=False)
    sale = models.IntegerField(blank=True, null=True, default=0)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product_name

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

# ======================================================================================================

# class ProductColor(models.Model):
#     name_color = models.ForeignKey(ProductColors, on_delete=models.CASCADE, null=True)
#     is_main =  models.BooleanField(default=False)
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     is_active = models.BooleanField(default=True)
#
#
#     def __str__(self):
#         return self.product.product_name
#
#     class Meta:
#         verbose_name = 'Цвет'
#         verbose_name_plural = 'Цвета'



class ProductImage(models.Model):
    is_main =  models.BooleanField(default=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='static/media/productsImg/')
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product.product_name

    class Meta:
        verbose_name = 'Фото'
        verbose_name_plural = 'Фотографии'