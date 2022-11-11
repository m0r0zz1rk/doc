from django.contrib import admin
from .models import *


@admin.register(DocKinds)
class DocKindsAdmin(admin.ModelAdmin):
    list_display = ('kind',)


@admin.register(DocTypes)
class DocTypesAdmin(admin.ModelAdmin):
    list_display = ('kind', 'type')


@admin.register(DocTypeCategories)
class DocTypeCategoriesAdmin(admin.ModelAdmin):
    list_display = ('type', 'category')


@admin.register(DocRequisiteTypes)
class DocRequisiteTypesAdmin(admin.ModelAdmin):
    list_display = ('req_type',)


@admin.register(DocTemplateRequisites)
class DocTemplateRequisitesAdmin(admin.ModelAdmin):
    list_display = ('req_type', 'requisite')

# Register your models here.
