from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.db.models import Q

User = get_user_model()

# Register your models here.

# https://realpython.com/manage-users-in-django-admin/
# https://github.com/pgorecki/django-cancan


# admin.site.unregister(User)


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if not request.user.is_superuser and request.user.is_staff:
            qs = qs.filter(Q(is_staff=False) | Q(Q(is_staff=True) & Q(is_superuser=False)))
        return qs
