from django.contrib import admin

from schedule.models import Cell, Day, Settings, Talon


@admin.register(Cell)
class CellAdminModel(admin.ModelAdmin):
    """Admin model for cell"""

    list_display = ('data', 'time_start', 'time_end')


@admin.register(Talon)
class TalonAdminModel(admin.ModelAdmin):
    """Admin model for talon"""

    list_display = ('user', 'data', 'time_start', 'time_end')


@admin.register(Day)
class DayAdminModel(admin.ModelAdmin):
    """Admin model for day"""

    list_display = ('name', 'worktime_start', 'worktime_end')


admin.site.register(Settings)
