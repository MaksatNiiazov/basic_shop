from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.

class SingletonModel(models.Model):
    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if self.__class__.objects.exists() and not self.pk:
            self.pk = self.__class__.objects.first().pk
        super(SingletonModel, self).save(*args, **kwargs)

    @classmethod
    def load(cls):
        if not cls.objects.exists():
            return cls.objects.create()
        return cls.objects.first()


class StaticPage(models.Model):
    title = models.CharField(max_length=200, unique=True, verbose_name=_('Заголовок'))
    slug = models.SlugField(max_length=200, unique=True, blank=True, verbose_name=_('Слаг'))
    content = models.TextField(verbose_name=_('Контент'))
    image = models.ImageField(upload_to='static_pages/', blank=True, null=True, verbose_name=_('Изображение'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Время создания'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Время обновления'))

    class Meta:
        verbose_name = _('Статическая страница')
        verbose_name_plural = _('Статические страницы')


class SiteSettings(SingletonModel):
    site_name = models.CharField(max_length=255, verbose_name="Название сайта")
    site_description = models.TextField(verbose_name="Описание сайта")

    class Meta:
        verbose_name = _("Настройки сайта")
        verbose_name_plural = _("Настройки сайта")

    def __str__(self):
        return self.site_name


class ContactInfo(SingletonModel):
    class Meta:
        verbose_name = _("Контактная информация")
        verbose_name_plural = _("Контактная информация")

    def __str__(self):
        return _("Контактная информация")


class Email(models.Model):
    contact = models.ForeignKey(ContactInfo, related_name='emails', on_delete=models.CASCADE,
                                verbose_name=_("Контактная информация"))
    email = models.EmailField(verbose_name=_("Электронная почта"))

    class Meta:
        verbose_name = _("Электронная почта")
        verbose_name_plural = _("Электронные почты")

    def __str__(self):
        return self.email


class PhoneNumber(models.Model):
    contact = models.ForeignKey(ContactInfo, related_name='phone_numbers', on_delete=models.CASCADE,
                                verbose_name=_("Контактная информация"))
    phone_number = models.CharField(max_length=20, verbose_name=_("Номер телефона"))

    class Meta:
        verbose_name = _("Номер телефона")
        verbose_name_plural = _("Номера телефонов")

    def __str__(self):
        return self.phone_number


class Address(models.Model):
    contact = models.ForeignKey(ContactInfo, related_name='addresses', on_delete=models.CASCADE, verbose_name=_("Контактная информация"))
    address = models.TextField(verbose_name=_("Адрес"))

    class Meta:
        verbose_name = _("Адрес")
        verbose_name_plural = _("Адреса")

    def __str__(self):
        return self.address


class SocialNetwork(models.Model):
    contact = models.ForeignKey(ContactInfo, related_name='social_networks', on_delete=models.CASCADE,
                                verbose_name=_("Контактная информация"))
    network_name = models.CharField(max_length=50, verbose_name=_("Название социальной сети"))
    url = models.URLField(verbose_name=_("URL"))

    class Meta:
        verbose_name = _("Социальная сеть")
        verbose_name_plural = _("Социальные сети")

    def __str__(self):
        return self.network_name
