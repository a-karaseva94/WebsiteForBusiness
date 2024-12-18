from django.contrib import admin
from .models import *

# Админка для CartItem
admin.site.register(CartItem)


# Админка для Service
@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    """
        Оформление админ-панели для услуг

        list_display указывает, какие столбцы отобразятся в списке объектов
        search_fields задает область поиска по указанным столбцам
        list_filter устанавливает фильтр по указанному столбцу
        list_per_page определяет количество объектов на странице
        fieldsets определяет открытые и скрытые элементы (скрыта стоимость)

    """
    list_display = ('title', 'type', 'program', 'cost',)
    search_fields = ('type', 'program',)
    list_filter = ('cost',)
    list_per_page = 5
    fieldsets = (
        (None, {
            'fields': ('title', 'type', 'program')
        }),

        ('Дополнительные настройки', {
            'classes': ('collapse',),  # скрытие секции - по умолчанию
            'fields': ('cost',)
        }),
    )