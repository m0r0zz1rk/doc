from django.contrib import admin

from authen.models import Profiles


@admin.register(Profiles)
class ProfilesAdmin(admin.ModelAdmin):
    list_display = ('surname', 'name', 'patronymic', 'phone')
# Register your models here.
