from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.db.models import Q

User = get_user_model()

# Register your models here.

# https://realpython.com/manage-users-in-django-admin/

admin.site.unregister(User)


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if not request.user.is_superuser and request.user.is_staff:
            qs = qs.filter(is_staff=False)
        return qs