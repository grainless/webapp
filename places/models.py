from django.contrib.gis.db import models


class Chain(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    lede = models.CharField(blank=True, max_length=100)
    description = models.TextField(blank=True, max_length=500)

    def __str__(self):
        return self.title


class Place(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    chain = models.ForeignKey(Chain, blank=True, null=True, on_delete=models.CASCADE)
    lede = models.CharField(blank=True, max_length=100)
    description = models.TextField(blank=True, max_length=500)
    location = models.PointField()

    def __str__(self):
        return self.title
