from django.contrib import admin
from users.models import User


class UserAdmin(admin.ModelAdmin):
    fields = (
        'first_name',
        'middle_name',
        'last_name',
    )

admin.site.register(User, UserAdmin)
