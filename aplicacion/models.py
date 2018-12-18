# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.template.defaultfilters import slugify
from django.utils import timezone

class Chocolate(models.Model):
    nombreC = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return str(self.nombreC)

    def __unicode__(self):
        return str(self.nombreC)

    class Meta:
        verbose_name_plural = "Chocolates"


class Ingrediente(models.Model):
    nombreI = models.CharField(max_length=128, unique=True, blank=True, null=True)

    def __str__(self):
        return str(self.nombreI)

    def __unicode__(self):
        return str(self.nombreI)


class Proporcion(models.Model):
    chocolate = models.ForeignKey(Chocolate)
    ingrediente = models.ForeignKey(Ingrediente)
    porcentaje = models.FloatField()

    def __str__(self):
        return "proporcion"

    def __unicode__(self):
        return u"proporcion"
