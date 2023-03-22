from django.contrib import admin
from form.models import Form

@admin.register(Form)
class FormAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('full_name', 'email', 'mobile')
    search_fields = ('full_name', 'email', 'mobile', 'created')
    date_hierarchy = 'created'