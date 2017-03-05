from django.contrib import admin
from .models import User
# Register your models here.
from django.contrib.auth.admin import UserAdmin


class MyUserAdmin(UserAdmin):
    model = User

    fieldsets = UserAdmin.fieldsets + (
            (None, {'fields':
                    ('department', 'specialization')
                    }
             ),
    )

admin.site.register(User, MyUserAdmin)