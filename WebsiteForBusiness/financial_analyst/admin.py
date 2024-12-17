from django.contrib import admin
from .models import *


# Админка для Buyer
@admin.register(Buyer)
class BuyerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email',)
    search_fields = ('name',)


# Админка для Services
@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'type', 'program', 'cost', )
    search_fields = ('type', 'program',)
    list_filter = ('cost', )
    list_per_page = 5  # количество на странице
    # Разбивка на секции
    fieldsets = (
        (None, {
            'fields': ('title', 'type', 'program')
        }),

        ('Дополнительные настройки', {
            'classes': ('collapse',), # скрытие секции по умолчанию
            'fields': ('cost',)
        }),
    )