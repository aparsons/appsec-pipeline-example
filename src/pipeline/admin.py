from django.contrib import admin

from . import models


class ApplicationAdmin(admin.ModelAdmin):
    list_display = ['name', 'platform', 'criticality', 'origin', 'lifecycle', 'active']
    list_filter = ['platform', 'criticality', 'origin', 'lifecycle', 'active']
    readonly_fields = ['created', 'modified']
    search_fields = ['^name']
admin.site.register(models.Application, ApplicationAdmin)
