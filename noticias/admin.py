# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Categoria, Noticia

# Register your models here.

admin.site.register(Categoria)
admin.site.register(Noticia)