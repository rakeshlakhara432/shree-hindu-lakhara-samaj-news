from django.contrib import admin
from .models import Event

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'venue', 'registration_limit', 'fees')
    list_filter = ('date',)
    search_fields = ('title', 'venue')
    prepopulated_fields = {'slug': ('title',)}
