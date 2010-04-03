from django.contrib import admin
from contact.models import Message

class MessageAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('name', 'from_email', 'message', 'created_date', 'responded_to',)
        }),
        ('Advanced Info', {
            'classes': ('collapse',),
            'fields' : ('ip',)
        }),
    )
    list_display = ('name', 'from_email', 'created_date','responded_to')
    list_editable = ('responded_to',)
    list_per_page = 50
    save_on_top = True
    search_fields = ('name', 'from_email',)
    
admin.site.register(Message, MessageAdmin)