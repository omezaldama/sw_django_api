from django.db import models

from sw_api.models.climate import Climate
from sw_api.models.terrain import Terrain


class Planet(models.Model):
    name = models.CharField(max_length=50, unique=True)
    population = models.BigIntegerField(null=True)
    climates = models.ManyToManyField(Climate)
    terrains = models.ManyToManyField(Terrain)
