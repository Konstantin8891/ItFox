from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group

from .models import Users
from .forms import UserChangeForm, UserCreationForm


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = (
        "username",
        "role"
    )

    list_filter = ('username', )
    ordering = ('id',)

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'username',
                'password1',
                'password2',
                'role'
            ),
        }),
    )

    fieldsets = (
        (None, {'fields': (
            'username',
            'password',
            'role'
        )}),
    )

    filter_horizontal = ()


admin.site.register(Users, UserAdmin)
admin.site.unregister(Group)
