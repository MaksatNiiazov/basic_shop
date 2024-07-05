from django.contrib import admin

from apps.shop.models import StaticPage, Email, PhoneNumber, Address, SocialNetwork, SiteSettings, ContactInfo


@admin.register(StaticPage)
class StaticPageAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'slug', 'content', 'image', 'created_at', 'updated_at']
    list_display_links = ['title', 'slug']


class EmailInline(admin.TabularInline):
    model = Email
    extra = 0


class PhoneNumberInline(admin.TabularInline):
    model = PhoneNumber
    extra = 0


class AddressInline(admin.TabularInline):
    model = Address
    extra = 0


class SocialNetworkInline(admin.TabularInline):
    model = SocialNetwork
    extra = 0


@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    list_display = ('site_name',)


@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    inlines = [EmailInline, PhoneNumberInline, AddressInline, SocialNetworkInline]


# admin.site.register(Email)
# admin.site.register(PhoneNumber)
# admin.site.register(Address)
# admin.site.register(SocialNetwork)
