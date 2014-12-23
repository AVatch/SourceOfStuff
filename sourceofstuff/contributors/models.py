from django.db import models
from django.contrib.auth.models import AbstractUser


class Contributor(AbstractUser):
    bio = models.TextField(blank=True, null=True)
    time_created = models.DateTimeField(auto_now_add=True,
                                        blank=True,
                                        null=True)

    def __str__(self):
        return self.username

    class Meta:
        ordering = ('time_created',)
