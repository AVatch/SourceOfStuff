from django.contrib import admin
from .models import Item, Reference


class ItemAdmin(admin.ModelAdmin):
    pass
admin.site.register(Item, ItemAdmin)


class ReferenceAdmin(admin.ModelAdmin):
    pass
admin.site.register(Reference, ReferenceAdmin)
