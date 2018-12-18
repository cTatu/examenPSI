# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from aplicacion.models import Chocolate, Ingrediente, Proporcion


class ChocolateAdmin(admin.ModelAdmin):
    list_display = ('id','nombreC',)

class IngredienteAdmin(admin.ModelAdmin):
    list_display = ('id','nombreI',)

class ProporcionAdmin(admin.ModelAdmin):
    list_display = ('id','chocolate', 'ingrediente','porcentaje')


admin.site.register(Chocolate, ChocolateAdmin)
admin.site.register(Ingrediente, IngredienteAdmin)
admin.site.register(Proporcion, ProporcionAdmin)
