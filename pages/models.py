# -*- coding: utf-8 -*-
from django.db import models
from ckeditor.fields import RichTextField
import pytils

class Page(models.Model):
    slug = models.SlugField(verbose_name=u'слаг', blank=True, unique=True)
    title = models.CharField(max_length=256, verbose_name=u'заголовок')
    content = RichTextField(blank=True, verbose_name=u'html-содержимое')  
    
    class Meta:
        verbose_name = u'статическая страница'
        verbose_name_plural = u'статические страницы'
        
    def __unicode__(self):
        return self.slug
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug=pytils.translit.slugify(self.title)
        super(Page, self).save(*args, **kwargs)
    
    @staticmethod
    def get_by_slug(page_name):
        try:
            page = Page.objects.get(slug=page_name)
            return {'title': page.title,
                    'content': page.content
                    }
        except:
            return None