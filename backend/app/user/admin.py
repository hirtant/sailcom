from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin


@admin.register(User)
class UserAdmin(UserAdmin):
    readonly_fields = ('date_joined',)
    # fields shown when creating a new instance
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2')}
         ),
    )
    # fields when reading / updating an instance
    fieldsets = (
        (None, {'fields': ('email', 'username', 'password')}),
        ('Personal info', {'fields': ('salutation', 'first_name', 'last_name', 'phone', 'mobile', 'date_of_birth',
                                      'favourite_lake')}),
        ('Address', {'fields': ('street', 'address_appendix', 'city', 'zip_code', 'country')}),
        ('Documents', {'fields': ('avatar', 'licence')}),
        ('Status', {'fields': ('licence_ok', 'entry_fee_paid', 'request_membership',
                               'is_member', 'membership_type')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
        ('Groups', {'fields': ('groups',)}),
    )

    # fields which are shown when looking at an list of instances
    list_display = ('email', 'first_name', 'last_name', 'is_staff')
    ordering = ('email',)
