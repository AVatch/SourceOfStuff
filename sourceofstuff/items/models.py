from django.db import models
from contributors.models import Contributor
from taggit.managers import TaggableManager


class Reference(models.Model):
    src = models.URLField()
    views = models.IntegerField(default=0)
    time_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.src

    class Meta:
        ordering = ('-time_created',)


class Item(models.Model):
    name = models.CharField(max_length=50)
    cover = models.ImageField(upload_to='items/', blank=True, null=True)
    summary = models.CharField(max_length=250)

    first_mentioned = models.CharField(max_length=20, blank=True, null=True)
    geographic_origin = models.CharField(blank=True, null=True, max_length=100)
    inventor = models.CharField(blank=True, null=True, max_length=100)

    origin_story = models.TextField()

    contributors = models.ManyToManyField(Contributor,
                                          related_name="item_contributors")
    raters = models.ManyToManyField(Contributor,
                                    related_name="item_raters",
                                    blank=True, null=True)

    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)

    tags = TaggableManager()

    time_created = models.DateTimeField(auto_now_add=True)
    last_accessed = models.DateTimeField(blank=True, null=True)
    last_modified = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('-time_created',)
