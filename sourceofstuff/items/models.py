from django.db import models
from contributors.models import Contributor


class Item(models.Model):
    name = models.CharField(max_length=100)
    first_mentioned = models.DateField(blank=True, null=True)
    geographic_origin = models.CharField(blank=True, null=True, max_length=100)
    inventor = models.CharField(blank=True, null=True, max_length=100)
    origin_story = models.TextField()
    contributors = models.ManyToManyField(Contributor)
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)
    time_created = models.DateTimeField(auto_now_add=True)
    last_accessed = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('-time_created',)


class Reference(models.Model):
    src = models.URLField()
    item = models.ForeignKey(Item)
    views = models.IntegerField(default=0)
    time_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.src

    class Meta:
        ordering = ('item',)
