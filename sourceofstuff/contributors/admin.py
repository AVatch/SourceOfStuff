from django.contrib import admin
from .models import Contributor


class ContributorAdmin(admin.ModelAdmin):
    pass
admin.site.register(Contributor, ContributorAdmin)
