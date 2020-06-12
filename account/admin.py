from django.contrib import admin

from django.contrib.auth.admin import UserAdmin

from account.models import Account

class AccountAdmin(UserAdmin):
    list_display = ('id','email', 'username', 'date_joined', 'last_login', 'is_active', 'is_admin', 'is_staff', 'is_superuser')
    search_fields = ('email', 'username')
    readonly_fields = ('date_joined', 'last_login')
    list_editable = ('is_active', 'is_admin', 'is_staff', 'is_superuser')
    list_display_links = ('id', 'email', 'username')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Account, AccountAdmin)


# Register your models here.
