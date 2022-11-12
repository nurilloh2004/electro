from django.db import models
from django.utils.translation import gettext_lazy as _
from parler.models import TranslatableModel, TranslatedFields

# Create your models here.
class Banner(TranslatableModel):
    translations = TranslatedFields(
        title=models.CharField(max_length=200, verbose_name=_('Title')),
    )
    image = models.ImageField(upload_to='photos/banners')


    def __str__(self):
        return str(self.image)

    class Meta:
        verbose_name = 'Banner'
        verbose_name_plural = 'Banners'


class Brand(models.Model):
    image = models.ImageField(upload_to='photos/brands')

    def __str__(self):
        return str(self.image)

    class Meta:
        verbose_name = 'Brand'
        verbose_name_plural = 'Brands'


class Clients(TranslatableModel):
    translations = TranslatedFields(
        title=models.CharField(max_length=200, verbose_name=_('Title')),
    )

    image = models.ImageField(upload_to='photos/clients')
    url = models.CharField(max_length=250, blank=True, verbose_name=_('url'))

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'


class AboutMainImage(models.Model):
    main_image = models.ImageField(upload_to='photos/about', verbose_name=_('Main Image'))

    def __str__(self):
        return str(('image'))

    class Meta:
        verbose_name = 'About Main Image'
        verbose_name_plural = 'About Main Image'

class AboutImages(TranslatableModel):
    translations = TranslatedFields(
        title=models.CharField(max_length=200, verbose_name=_('Title')),
        description=models.TextField(max_length=200, verbose_name=_('Description')),
    )
    image = models.ImageField(upload_to='photos/about', blank=True, null=True, verbose_name=_('Image'))
    

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name = 'About'
        verbose_name_plural = 'About'


class Partners(models.Model):
    image = models.ImageField(upload_to='photos/about', verbose_name=_('Image 1'))
    url = models.CharField(max_length=250, blank=True, null=True, verbose_name=_('Link'))

    def __str__(self):
        return str(self.image)

    class Meta:
        verbose_name = 'Partners'
        verbose_name_plural = 'Partners'

class Team(TranslatableModel):
    translations = TranslatedFields(
        name = models.CharField(max_length=250, verbose_name=_('Name')),
        position = models.CharField(max_length=250, verbose_name=_('Position')),
        email = models.CharField(max_length=250, verbose_name=_('Email')),
    )

    image = models.ImageField(upload_to='photos/about', verbose_name=_('Image 1'))
    phone = models.CharField(max_length=250, blank=True, null=True, verbose_name=_('Phone'))
    telegram = models.CharField(max_length=250, blank=True, null=True, verbose_name=_('Telegram'))
    instagram = models.CharField(max_length=250, blank=True, null=True, verbose_name=_('Instagram'))

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'Team'
        verbose_name_plural = 'Team'



class Hitofsales(models.Model):
    image = models.ImageField(upload_to='photos/about', blank=True, null=True, verbose_name=_('Image 1'))

    def __str__(self):
        return str(('image'))

    class Meta:
        verbose_name = _('Hit Of Sales')
        verbose_name_plural = _('Hit Of Sales')