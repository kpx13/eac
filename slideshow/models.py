# -*- coding: utf-8 -*-
from django.db import models

class Slider(models.Model):
    image = models.FileField(upload_to= 'uploads/slider', max_length=256, verbose_name=u'картинка')
    text = models.CharField(max_length=512, verbose_name=u'текст')
    sort_parameter = models.IntegerField(default=0, blank=True, verbose_name=u'параметр для сортировки')
    
    class Meta:
        verbose_name = 'картинка в слайдере'
        verbose_name_plural = 'картинки в слайдере'
        ordering = ['sort_parameter']
    
    def __unicode__(self):
        return str(self.image)