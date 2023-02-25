from django.contrib import admin

from django.contrib import admin
from webapp.models import GBook


class GBookAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'created_at')
    list_filter = ('id', 'name', 'email', 'created_at')
    search_fields = ('name', 'email')
    fields = ('text', 'name', 'email', 'created_at')
    readonly_fields = ('id', 'created_at', 'updated_at')


admin.site.register(GBook, GBookAdmin)