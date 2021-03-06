# from django.contrib import admin
# from order.models import Order
# 
# class OrderAdmin(admin.ModelAdmin):
#     fieldsets = (
#         (None, {
#             'fields': ('name', 'from_email', 'message', 'responded_to',)
#         }),
#         ('Advanced Info', {
#             'classes': ('collapse',),
#             'fields' : ('ip',)
#         }),
#     )
#     list_display = ('name', 'from_email', 'responded_to')
#     list_editable = ('responded_to',)
#     list_per_page = 50
#     save_on_top = True
#     search_fields = ('name', 'from_email',)
#     
# admin.site.register(Order, OrderAdmin)