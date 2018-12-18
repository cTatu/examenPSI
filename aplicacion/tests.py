# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from django.core.urlresolvers import reverse
from django.contrib.staticfiles import finders
from django.test import Client
from aplicacion.models import Chocolate, Ingrediente, Proporcion

class AplicacionTests(TestCase):
    def setUp(self):
        # The test client is a Python class that acts as a dummy Web browser

        self._client   = Client()

    def add_chocolate(self, id, nombre):
        Chocolate.objects.get_or_create(id=id, nombreC=nombre)

    def add_ingrediente(self, id, nombre):
        Ingrediente.objects.get_or_create(id=id, nombreI=nombre)

    def add_proporcion(self, id, chocoalte_id, ingrediente_id, porcentaje):
        c = Chocolate.objects.get(id=chocoalte_id)
        i = Ingrediente.objects.get(id=ingrediente_id)
        Proporcion.objects.get_or_create(id=id, chocolate=c, ingrediente=i, porcentaje=porcentaje)


    def test_examen(self):
        print '    Borrando todos los objetos de la base de datos'
        Proporcion.objects.all().delete()
        Ingrediente.objects.all().delete()
        Chocolate.objects.all().delete()

        self.assertEqual(len(Proporcion.objects.all()), 0)
        self.assertEqual(len(Ingrediente.objects.all()), 0)
        self.assertEqual(len(Chocolate.objects.all()), 0)

        print '    Creando chocolate1'
        self.add_chocolate(1001, 'chocolate1')
        print '    Creando ingrediente1'
        self.add_ingrediente(1, 'ingrediente1')
        print '    Creando ingrediente2'
        self.add_ingrediente(2, 'ingrediente2')
        print '    Creando proporcion1'
        self.add_proporcion(1, 1001,2,.5)

        ingredientes = Ingrediente.objects.all()
        self.assertEqual(len(ingredientes), 2)
        self.assertEqual(ingredientes[0].id, 1)
        self.assertEqual(ingredientes[0].nombreI, 'ingrediente1')
        self.assertEqual(ingredientes[1].id, 2)
        self.assertEqual(ingredientes[1].nombreI, 'ingrediente2')
        print '    Ingredientes creados correctamente'

        chocoaltes = Chocolate.objects.all().order_by('id')
        self.assertEqual(len(chocoaltes), 1)
        self.assertEqual(chocoaltes[0].id, 1001)
        self.assertEqual(chocoaltes[0].nombreC, 'chocolate1')
        print '    Chocolates creadas correctamente'

        proporciones = Proporcion.objects.all()
        self.assertEqual(len(proporciones), 1)
        self.assertEqual(proporciones[0].id, 1)
        self.assertEqual(proporciones[0].chocolate.id, 1001)
        self.assertEqual(proporciones[0].ingrediente.id, 2)
        self.assertEqual(proporciones[0].porcentaje, .5)
        print '    Proporcion creada correctamente'

        response = self._client.post(reverse('chocolate'))

        print '    Comprobando resultados devueltos por la vista'
        self.assertIn('chocolate1', str(response.content).decode('utf-8'))
        self.assertIn('1001', str(response.content).decode('utf-8'))
        self.assertIn('ingrediente2', str(response.content).decode('utf-8'))
        print '    Resultados ok'
