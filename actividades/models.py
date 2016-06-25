from __future__ import unicode_literals

from django.db import models

# Modelo de actividades
class actividadesModel(models.Model):

	class Meta:
		verbose_name = 'Actividad'
		verbose_name_plural = 'Actividades'

	nombre = models.CharField(max_length=100, blank=False, null=False)
	slug = models.SlugField()
	imagen = models.CharField(max_length=50)

	def __str__(self):
		return u'%s' % (self.nombre)

	def __unicode__(self):
		return u'%s' % (self.nombre)