from django.contrib import admin
from eagleproject.models import Participant, Work#, Donation

class ParticipantAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('name', 'email', 'role', 'work')
        }),
        # ('Advanced Info', {
        #     'classes': ('collapse',),
        #     'fields' : ('created_date', 'slug',)
        # }),
    )
    list_display = ('name', 'email')
    list_per_page = 50
    save_on_top = True
    search_fields = ('name', 'email',)

class WorkAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('title', 'description', 'hours', 'date',)
        }),
        # ('Advanced Info', {
        #     'classes': ('collapse',),
        #     'fields' : ('slug',)
        # }),
    )
    list_display = ('title', 'date', 'hours',)
    list_per_page = 50
    save_on_top = True
    search_fields = ('title', 'description',)

# class DonationAdmin(admin.ModelAdmin):
#     fieldsets = (
#         (None, {
#             'fields': ('title', 'description', 'hours', 'date',)
#         }),
#         # ('Advanced Info', {
#         #     'classes': ('collapse',),
#         #     'fields' : ('slug',)
#         # }),
#     )
#     list_display = ('title', 'date', 'hours',)
#     list_per_page = 50
#     save_on_top = True
#     search_fields = ('title', 'description',)
    
admin.site.register(Participant, ParticipantAdmin)
admin.site.register(Work, WorkAdmin)
# admin.site.register(Donation, DonationAdmin)