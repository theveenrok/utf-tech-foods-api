from django.contrib import admin
from django.contrib.admin import ModelAdmin, register

from apps.menu.models import Food, FoodCategory


@register(Food)
class FoodAdmin(ModelAdmin):
    list_display = ("id", "category", "name_ru", "description_ru", "cost", "is_publish")
    list_display_links = ("id",)
    list_editable = ("is_publish",)
    inlines = ()


admin.site.register(FoodCategory)
