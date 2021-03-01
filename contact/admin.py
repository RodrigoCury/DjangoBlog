from django.contrib import admin
from .models import Messages

# Register your models here.


@admin.register(Messages)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'subject', 'created')
    list_filter = ('created', 'name', 'subject')
    date_hierarchy = 'created'
    readonly_fields = ('name', 'subject', 'message')
