from django.contrib import admin
from .models import URL
class URLAdmin(admin.ModelAdmin):
    list_display = ('original_url', 'short_code', 'access_count')
admin.site.register(URL, URLAdmin)