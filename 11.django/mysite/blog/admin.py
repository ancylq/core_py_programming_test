# coding:utf-8
from django.contrib import admin

# Register your models here.
from blog import models

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'timestemp') # 列表页显式的字段

admin.site.register(models.BlogPost, BlogPostAdmin)