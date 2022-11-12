from django.contrib import admin
from .models import *
from parler import admin as parler_admin
from parler.admin import TranslatableAdmin
from django.utils.safestring import mark_safe


# Register your models here.

class AboutAdmin(TranslatableAdmin):
    list_display = ('title',)


admin.site.register(AboutImages, AboutAdmin)


class AboutMainAdmin(admin.ModelAdmin):
    pass



admin.site.register(AboutMainImage, AboutMainAdmin)


class HitAdmin(admin.ModelAdmin):
    list_display = ('get_image',)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="auto" height="60"')



admin.site.register(Hitofsales, HitAdmin)


class BrandAdmin(admin.ModelAdmin):
    list_display = ('get_image',)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="auto" height="60"')


admin.site.register(Brand, BrandAdmin)

class PartnersAdmin(admin.ModelAdmin):
    list_display = ('get_image',)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="auto" height="60"')


admin.site.register(Partners, PartnersAdmin)

class TeamAdmin(TranslatableAdmin):
    list_display = ('get_image', 'name')

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="auto" height="60"')


admin.site.register(Team, TeamAdmin)

@admin.register(Clients)
class Clients(TranslatableAdmin):
    pass


@admin.register(Banner)
class Banner(TranslatableAdmin):
    pass
