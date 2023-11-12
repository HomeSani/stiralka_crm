from datetime import datetime, time

from django.contrib.auth.models import User
from django.db import models


class Talon(models.Model):
    """Model for talon"""

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name='Пользователь, занявший время'
    )
    date = models.DateField(
        default=datetime.now, verbose_name='Дата дня для стирки', blank=True
    )
    week_id = models.IntegerField(default=0, blank=True)
    day_id = models.IntegerField(default=0, blank=True)
    time_start = models.TimeField(verbose_name='Начало стирки')
    time_end = models.TimeField(verbose_name='Окончание стирки')

    class Meta:
        """Meta class for model"""

        verbose_name = 'Талон'
        verbose_name_plural = 'Талоны'

    def save(self, *args, **kwargs) -> None:
        """Method calling when model be saved"""
        self.week_id = self.date.isocalendar()[1]
        self.day_id = self.date.weekday()
        super(Talon, self).save(*args, **kwargs)

    def __str__(self) -> str:
        """Return info, when called(in admin panel)"""
        return f'Cell({self.user} - {self.date}): {self.time_start} - {self.time_end}'


class Day(models.Model):
    """Model for weekday"""

    index = models.PositiveIntegerField(
        unique=True, verbose_name='Индекс дня недели(0 - 6)'
    )
    name = models.CharField(max_length=32, verbose_name='Название дня недели')
    worktime_start = models.TimeField(
        default=time(hour=6, minute=0), verbose_name='Начало работы стирки'
    )
    worktime_end = models.TimeField(
        default=time(hour=23, minute=0), verbose_name='Окончание работы стирки'
    )

    class Meta:
        """Meta class for model"""

        verbose_name = 'День'
        verbose_name_plural = 'Дни'

    def __str__(self) -> str:
        """Return info, when called(in admin panel)"""
        return f"{self.name}: {self.worktime_start} - {self.worktime_end}"


class Settings(models.Model):
    """Model for schedule settings"""

    available_days = models.ManyToManyField(Day, verbose_name='Дни недели для стирки')
    wash_duration = models.PositiveIntegerField(
        default=1, verbose_name='Время стирки(одной) в часах'
    )

    class Meta:
        """Meta class for model"""

        verbose_name = 'Настройки'
        verbose_name_plural = 'Настройки'

    def __str__(self) -> str:
        """Return info, when called(in admin panel)"""
        return 'Настройки'
