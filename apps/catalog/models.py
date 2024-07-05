from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from mptt.models import MPTTModel, TreeForeignKey
from unidecode import unidecode


class Category(MPTTModel):
    name = models.CharField(max_length=255, verbose_name=_('Название'))
    slug = models.SlugField(max_length=255, unique=True, blank=True, null=True, verbose_name=_('Слаг'))
    image = models.ImageField(null=True, blank=True, verbose_name=_('Изображение'))
    parent = TreeForeignKey("self", on_delete=models.SET_NULL, null=True, blank=True,
                            related_name="children", verbose_name=_("Родительская категория"))
    order = models.PositiveIntegerField(default=0, editable=False, db_index=True, verbose_name=_('Порядок'))

    class MPTTMeta:
        order_insertion_by = ["name"]

    class Meta:
        verbose_name = _("Категория")
        verbose_name_plural = _("Категории")
        ordering = ['order', 'name']

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(unidecode(self.name))
            unique_slug = base_slug
            counter = 1
            while Category.objects.filter(slug=unique_slug).exists():
                unique_slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = unique_slug
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.name}'


class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name=_("Название продукта"))
    description = models.TextField(blank=True, null=True, verbose_name=_("Описание"))
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_("Цена"))
    stock = models.PositiveIntegerField(verbose_name=_("Количество на складе"))
    category = models.ForeignKey(Category, related_name='products', on_delete=models.PROTECT,
                                 verbose_name=_("Категория"))
    is_active = models.BooleanField(default=True, verbose_name=_("Активен"))

    class Meta:
        verbose_name = _("Продукт")
        verbose_name_plural = _("Продукты")

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images', verbose_name=_("Продукт"))
    image = models.ImageField(upload_to='product_images', verbose_name=_("Картинка"), max_length=1000)
    main = models.BooleanField(default=False, verbose_name=_("Основное изображение"))

    class Meta:
        verbose_name = _("Изображение продукта")
        verbose_name_plural = _("Изображения продуктов")

    def __str__(self):
        return f"{self.product.name} Image"
