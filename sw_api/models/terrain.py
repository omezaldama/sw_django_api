from django.db import models


class Terrain(models.Model):
    name = models.CharField(max_length=50)
