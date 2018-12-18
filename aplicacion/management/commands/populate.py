import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'proyecto.settings')

import django

django.setup()
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from aplicacion.models import Chocolate, Ingrediente, Proporcion

class Command(BaseCommand):
    def handle(self, *args, **options):
        Chocolate.objects.all().delete()
        Ingrediente.objects.all().delete()
        Proporcion.objects.all().delete()

        self.add_chocolate(1001, 'chocolate_a')
        self.add_chocolate(1002, 'chocolate_b')
        self.add_chocolate(1003, 'chocolate_c')

        self.add_ingrediente(1001, 'ingrediente_a')
        self.add_ingrediente(1002, 'ingrediente_b')
        self.add_ingrediente(1003, 'ingrediente_c')
        self.add_ingrediente(1004, 'ingrediente_d')

        self.add_proporcion(1001, 1001, 1001, .2)
        self.add_proporcion(1002, 1002, 1002, .2)
        self.add_proporcion(1003, 1002, 1003, .3)
        self.add_proporcion(1004, 1001, 1003, .4)

    def add_chocolate(self, id, nombre):
        Chocolate.objects.get_or_create(id=id, nombreC=nombre)

    def add_ingrediente(self, id, nombre):
        Ingrediente.objects.get_or_create(id=id, nombreI=nombre)

    def add_proporcion(self, id, chocoalte_id, ingrediente_id, porcentaje):
        c = Chocolate.objects.get(id=chocoalte_id)
        i = Ingrediente.objects.get(id=ingrediente_id)
        Proporcion.objects.get_or_create(id=id, chocolate=c, ingrediente=i, porcentaje=porcentaje)
