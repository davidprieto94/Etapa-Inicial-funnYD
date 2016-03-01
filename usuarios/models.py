from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


GENEROS = (
		('M', 'Masculino'),
		('F', 'Femenino'),
	)

class usuariosModel(models.Model):
	user = models.OneToOneField(User)
	slug = models.SlugField()
	documento = models.PositiveIntegerField(null=True, blank=True)
	genero = models.CharField(max_length=2, choices=GENEROS, null=False, blank=False)
	fnacimiento = models.DateField()

	def __str__(self):
		return u'%s' % (self.user)

	def __unicode__(self):
		return u'%s' % (self.user)