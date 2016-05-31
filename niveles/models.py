from __future__ import unicode_literals

from django.db import models
from actividades.models import actividadesModel

# Modelo de niveles
class nivelesModel(models.Model):

	class Meta:
		verbose_name ='Nivel'
		verbose_name_plural = 'Niveles'

	nombre = models.CharField(max_length=100, blank=False, null=False)
	slug = models.SlugField()
	juego = models.CharField(max_length=50, blank=False, null=False)
	actividad = models.ForeignKey(actividadesModel)

	def __str__(self):
			return u'%s' % (self.nombre)

	def __unicode__(self):
			return u'%s' % (self.nombre)
