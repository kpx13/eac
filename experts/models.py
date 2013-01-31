# -*- coding: utf-8 -*-
from django.db import models

class Expert(models.Model):
    name = models.CharField(max_length=256, verbose_name=u'имя')
    content = models.TextField(blank=True, verbose_name=u'описание')

    class Meta:
        verbose_name = u'эксперт'
        verbose_name_plural = u'эксперты'
        
    def __unicode__(self):
        return self.name