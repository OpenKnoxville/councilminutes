# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from citycouncil.models import Decision


class DecisonAdmin(admin.ModelAdmin):
    list_display = ('code', 'text', )
    search_fields = ('code', 'text', )

admin.site.register(Decision, DecisonAdmin)
