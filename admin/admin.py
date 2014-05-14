# -*- coding: utf-8 -*-
__author__ = 'mauricio'

from django.contrib import admin
from django.contrib.sites.models import Site
#models
from newsletter.models import Body,Area,Map,Imagen, ImagenMap

#forms
from newsletter.forms import FormBody

class AdminBody(admin.ModelAdmin):
    list_display = ('name','text')

    class Media:
        js = (
            '/media/js/tinymce/jscripts/tiny_mce/tiny_mce.js',
              )
        
admin.site.register(Body,AdminBody)
admin.site.register(Area)
admin.site.register(Map)
admin.site.register(Imagen)
admin.site.register(ImagenMap)
#admin.site.unregister(Site)
