# -*- coding: utf-8 -*-
from django.contrib import admin
from django.utils.translation import ugettext as _
from .models import ImageSlider, ImageSliderItem

class ImageSliderItemInline(admin.TabularInline):
    model = ImageSliderItem
    fields = ('render_preview', 'image', 'title', 'alt', 'ordering', )
    readonly_fields = ('render_preview', 'ordering', )
    extra = 0

    def render_preview(self, news_image):
        url = news_image.image['preview'].url
        if url:
            return u'<img src="%s">' % url
        else:
            return u''

    render_preview.allow_tags = True
    render_preview.short_description = _(u'Preview')


class ImageSliderAdmin(admin.ModelAdmin):
    inlines = [ImageSliderItemInline]

admin.site.register(ImageSlider, ImageSliderAdmin)
