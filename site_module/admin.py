from django.contrib import admin
from . import models


class FooterLinkAdmin(admin.ModelAdmin):
    list_display = ['title', 'url']


class GalleryAdmin(admin.ModelAdmin):
    list_display = ['title']



admin.site.register(models.GalleryPhoto, GalleryAdmin)
admin.site.register(models.SiteSetting)
admin.site.register(models.FooterLinkBox)
admin.site.register(models.FooterLink, FooterLinkAdmin)
