# -*- coding: utf-8 -*-
from django.contrib import admin
import models

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'text')
    search_fields = ('name', 'text')

admin.site.register(models.Project, ArticleAdmin)