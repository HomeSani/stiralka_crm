from django.contrib import admin

from schedule.models import Cell, Day, Settings


@admin.register(Cell)
class Admin(admin.ModelAdmin):
    list_display = ('user', 'data', 'time_start', 'time_end')


@admin.register(Day)
class Admin(admin.ModelAdmin):
    list_display = ('name', 'worktime_start', 'worktime_end')


admin.site.register(Settings)
