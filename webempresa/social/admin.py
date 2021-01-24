from django.contrib import admin
from .models import Link

# Register your models here.
class LinkAdmin(admin.ModelAdmin):
    list_display = ('key', 'name', 'url')
    readonly_fields = ('created', 'updated')

admin.site.register(Link, LinkAdmin)