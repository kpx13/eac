# -*- coding: utf-8 -*-
from django.db import models
from django.db.models import Q
import pytils
from ckeditor.fields import RichTextField


class Article(models.Model):
    slug = models.SlugField(verbose_name=u'название', blank=True, unique=True)
    name = models.CharField(max_length=128, verbose_name=u'название')
    image = models.FileField(upload_to= 'uploads/news', blank=True, max_length=256, verbose_name=u'картинка')
    date = models.DateField(verbose_name=u'дата')
    text = RichTextField(verbose_name=u'полный текст')
   
    class Meta:
        verbose_name = u'новость'
        verbose_name_plural = u'новости'
        ordering = ['-date']
    
    def __unicode__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug=pytils.translit.slugify(self.name)
        super(Article, self).save(*args, **kwargs)
    
    @staticmethod
    def recent_some(count):
        try:
            return Article.objects.all()[:count]
        except:
            return ""
        
    @staticmethod
    def get_by_slug(page_name):
        try:
            return Article.objects.get(slug=page_name)
        except:
            return None
        
    @staticmethod
    def find(value):
        return Article.objects.filter(Q(name__contains=value) | Q(text__contains=value))
        