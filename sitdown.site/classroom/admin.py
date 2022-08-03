from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import (Classroom, Gender, Location, Requirement, Schoolboy,
                     Teacher)


class RequirementAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "comment")
    prepopulated_fields = {"slug": ("name",)}


class SchoolboyAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "slug",
        "phone",
        "date_of_birth",
        "comment",
        "classroom",
        "gender",
        "requirement",
        "energy",
        "height",
        "get_photo",
    )
    list_filter = (
        "name",
        "classroom",
        "date_of_birth",
        "gender",
        "requirement",
        "energy",
        "height",
    )
    search_fields = ("name", "body")
    prepopulated_fields = {"slug": ("name",)}
    date_hierarchy = "date_of_birth"
    ordering = ("name",)

    def get_photo(self, obj):
        return mark_safe(f'<img src="{obj.photo.url}" width="50">')

    get_photo.short_description = "Миниатюра"


class GenderAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    prepopulated_fields = {"slug": ("name",)}
    list_filter = ("name",)


class ClassroomAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "comment")
    list_filter = ("name",)
    search_fields = ("name",)
    ordering = ("name",)
    prepopulated_fields = {"slug": ("name",)}


class LocationAdmin(admin.ModelAdmin):
    list_display = ("position", "save_bd", "classroom", "create_data", "end_data")


class TeacherAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "classroom", "photo", "comment", "position")
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Requirement, RequirementAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Schoolboy, SchoolboyAdmin)
admin.site.register(Gender, GenderAdmin)
admin.site.register(Classroom, ClassroomAdmin)
admin.site.register(Location, LocationAdmin)
