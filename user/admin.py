from django.contrib import admin
from .models import Account


# Register your models here.
class AccountAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'username', 'last_login', 'is_active','date_joined')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
    readonly_fields = ('last_login', 'date_joined')
    ordering = ('-date_joined',)
    



admin.site.register(Account, AccountAdmin)
