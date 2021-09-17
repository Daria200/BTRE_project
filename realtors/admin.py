from django.contrib import admin
from .models import Realtor

class RealtorAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_mvp', 'hire_date', 'phone', 'email')
    list_editable = ('is_mvp',)
    list_filter = ('name',)
    search_fields = ('name', 'phone', 'email')
    list_display_links = ('name', 'phone')
    list_per_page = 25


admin.site.register(Realtor, RealtorAdmin)
