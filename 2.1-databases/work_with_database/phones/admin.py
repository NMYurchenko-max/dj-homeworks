from django.contrib import admin
from .models import Phone


@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'release_date', 'lte_exists')
    # Поля, отображаемые в списке телефонов

    list_filter = ('lte_exists',)
    # Поле для фильтрации по LTE

    search_fields = ('name', 'price')
    # Поля для поиска