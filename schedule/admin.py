from django.contrib import admin

from schedule.models import Cell, Day, Settings


@admin.register(Day)
class DayAdmin(admin.ModelAdmin):
    list_display = (
        'index',
        'start_time',
        'end_time',
    )


@admin.register(Cell)
class CellAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'start_time',
        'end_time',
        'date',
        'is_occupied',
    )
    list_editable = ('is_occupied',)
    date_hierarchy = 'date'
    list_filter = ('is_occupied',)


@admin.register(Settings)
class SettingsAdmin(admin.ModelAdmin):
    pass
