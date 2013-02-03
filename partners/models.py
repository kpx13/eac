# -*- coding: utf-8 -*-
from django.db import models

class Partner(models.Model):
    name = models.CharField(max_length=128, verbose_name=u'название')
    image = models.FileField(upload_to= 'uploads/partners', blank=True, max_length=256, verbose_name=u'логотип')
    desc = models.TextField(blank=True, verbose_name=u'краткое описание')
   
    class Meta:
        verbose_name = u'партнер'
        verbose_name_plural = u'партнеры'
        ordering = ['name']
    
    def __unicode__(self):
        return self.name