from cms.models.pluginmodel import CMSPlugin
from django.db import models
from django.utils.translation import ugettext as _
from easy_thumbnails.fields import ThumbnailerImageField
from easy_thumbnails.files import get_thumbnailer
from easy_thumbnails.exceptions import InvalidImageFormatError
import settings

class ImageSlider(CMSPlugin):
    title = models.CharField(
        max_length=200,
        blank=True,
        verbose_name=_(u'Title'))

    subtitle = models.CharField(
        max_length=200,
        blank=True,
        verbose_name=_(u'Subtitle'))

    def copy_relations(self, old_instance):
        for item in old_instance.images.all():
            item.pk = None
            item.slider = self
            item.save()

    class Meta:
        verbose_name = _(u'Image-Slider')
        verbose_name_plural = _(u'Image-Sliders')


class ImageSliderItem(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_(u'Created at'))

    slider = models.ForeignKey(ImageSlider,
        related_name='images',
        verbose_name=_(u'Image Slider'))

    ordering = models.PositiveIntegerField(
        default=0,
        verbose_name=_(u'Ordering'))

    image = ThumbnailerImageField(
        upload_to='news_image/',
        verbose_name=_(u'Image'))

    image_width = models.PositiveSmallIntegerField(
        default=0,
        null=True,
        verbose_name=_(u'Original Image Width'))

    image_height = models.PositiveSmallIntegerField(
        default=0,
        null=True,
        verbose_name=_(u'Original Image Height'))

    title = models.CharField(
        blank=True,
        default='',
        max_length=150,
        verbose_name=_(u'Image Title'))

    alt = models.CharField(
        blank=True,
        default='',
        max_length=150,
        verbose_name=_(u'Alternative Image Text'))

    def save(self):
        if self.ordering is None:
            self.ordering = self.slider.images.count()
        super(ImageSliderItem, self).save()


    def _get_image(self, image_format):
        _image_format = settings.THUMBNAIL_ALIASES[''][image_format]
        _img = self.image
        try:
            img = get_thumbnailer(_img).get_thumbnail(_image_format)
            return {
                'url': img.url,
                'width': img.width,
                'height': img.height,
                'alt': self.alt,
                'title': self.title,
            }
        except (UnicodeEncodeError, InvalidImageFormatError):
            return None

    class Meta:
        verbose_name = _(u'Image-Slider Item')
        verbose_name_plural = _(u'Image-Slider Items')
