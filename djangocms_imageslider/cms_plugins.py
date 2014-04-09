from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _

from .models import ImageSlider
from .admin import ImageSliderItemInline

class ImageSliderPlugin(CMSPluginBase):
    model = ImageSlider
    name = _("Image Slider")
    render_template = "cms/plugins/imageslider/slider.html"

    inlines = [ImageSliderItemInline]

    def render(self, context, instance, placeholder):
        context['instance'] = instance
        context['images'] = list(instance.images.all())
        return context

plugin_pool.register_plugin(ImageSliderPlugin)
