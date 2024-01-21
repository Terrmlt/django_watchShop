from django.contrib import admin

from .models import Brand, Watch, WatchImage

admin.site.register(Brand)


class WatchImageInline(admin.TabularInline):
    model = WatchImage
    extra = 3


@admin.register(Watch)
class WatchAdmin(admin.ModelAdmin):
    inlines = [WatchImageInline, ]
