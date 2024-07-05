from django.contrib import admin
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _
from mptt.admin import DraggableMPTTAdmin

from apps.catalog.models import Category, Product, ProductImage


@admin.register(Category)
class CategoryAdmin(DraggableMPTTAdmin):
    list_display = [
        "tree_actions",
        "indented_name",
        "parent",
    ]
    list_display_links = ("indented_name",)
    list_filter = [
        "parent"
    ]
    search_fields = ["id", 'name']
    list_select_related = ["parent"]
    mptt_level_indent = 20

    @admin.display(description="Название")
    def indented_name(self, instance):
        return mark_safe(
            '<div style="text-indent: {}px">{}</div>'.format(
                instance._mpttfield('level') * self.mptt_level_indent,
                instance.name
            )
        )


class ProductImageInline(admin.StackedInline):
    model = ProductImage
    extra = 0
    readonly_fields = ('image_preview',)
    fields = ['image_preview', 'image', 'main', ]

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-width:150px;" />', obj.image.url)
        return _("Нет изображения")

    image_preview.short_description = _("Предварительный просмотр")


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock', 'category', 'is_active', 'main_image')
    list_filter = ('category', 'is_active')
    search_fields = ('name', 'description')
    inlines = [ProductImageInline]

    def main_image(self, obj):
        main_image = obj.images.filter(main=True).first()
        if main_image:
            return format_html('<img src="{}" style="max-width:150px;" />', main_image.image.url)
        elif obj.images:
            image = obj.images.all().first()
            return format_html('<img src="{}" style="max-width:150px;" />', image.image.url)
        return _("Нет изображения")

    main_image.short_description = _("Основное изображение")


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    pass
