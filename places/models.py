from django.contrib.gis.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


class Entity(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    lede = models.CharField(blank=True, max_length=100)
    description = models.TextField(blank=True, max_length=500)

    def __str__(self):
        return self.title

    class Meta:
        abstract = True


class Chain(Entity):
    pass


class Place(Entity):
    chain = models.ForeignKey(Chain, blank=True, null=True, on_delete=models.CASCADE)
    location = models.PointField()
