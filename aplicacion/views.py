# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse

from django.shortcuts import render
from aplicacion.models import Chocolate, Ingrediente, Proporcion
from django.core.exceptions import ObjectDoesNotExist

def chocolate(request):
    chocolate = None
    nombreC = None
    error = None
    ingredientes = []

    try:
        chocolate = Chocolate.objects.get(id=1001)
        nombreC = chocolate.nombreC

        proporciones = Proporcion.objects.filter(chocolate=chocolate)
        if(len(proporciones) < 1):
            error = 'Este chocolate no tiene ingredientes'
        id_ingredientes = []
        porcentaje_ingredientes = []
        for proporcion in proporciones:
            if not proporcion.ingrediente.id in id_ingredientes:
                ingredientes.append(proporcion.ingrediente)
                id_ingredientes.append(proporcion.ingrediente.id)
    except ObjectDoesNotExist:
        error = 'Prenda con id 1003 no encontrada'

    _dict = {
        'error':error,
        'nombreC':nombreC,
        'ingredientes':ingredientes
    }

    return render(request, 'aplicacion/chocolate.html', context=_dict)
