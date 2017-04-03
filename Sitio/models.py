from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Noticia(models.Model):
	titulo = models.CharField(max_length=50)
	texto = models.CharField(max_length=200)
	fecha = models.DateTimeField()
	archivada = models.BooleanField(default = False)

