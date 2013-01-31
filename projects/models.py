# -*- coding: utf-8 -*-
from django.db import models
import pytils
from ckeditor.fields import RichTextField

class Project(models.Model):
    slug = models.SlugField(verbose_name=u'слаг', unique=True)
    name = models.CharField(max_length=128, verbose_name=u'название')
    image = models.FileField(upload_to= 'uploads/projects', blank=True, max_length=256, verbose_name=u'картинка')
    date = models.DateField(verbose_name=u'дата')
    desc = models.TextField(verbose_name=u'краткое описание')
    text = RichTextField(verbose_name=u'полный текст')
   
    class Meta:
        verbose_name = u'проект'
        verbose_name_plural = u'проекты'
        ordering = ['-date']
    
    def __unicode__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug=pytils.translit.slugify(self.name)
        super(Project, self).save(*args, **kwargs)
    
    @staticmethod
    def recent_some(count):
        try:
            return Project.objects.all()[:count]
        except:
            return ""
        
    @staticmethod
    def get_by_slug(page_name):
        try:
            return Project.objects.get(slug=page_name)
        except:
            return None