from django.contrib.auth.models import User
from django.db import models


class Day(models.Model):
    MONDAY_INDEX = 0
    THURSDAY_INDEX = 1
    WEDNESDAY_INDEX = 2
    TUESDAY_INDEX = 3
    FRIDAY_INDEX = 4
    SATURDAY_INDEX = 5
    SUNDAY_INDEX = 6

    DAY_CHOICES = (
        (MONDAY_INDEX, 'Понедельник'),
        (THURSDAY_INDEX, 'Вторник'),
        (WEDNESDAY_INDEX, 'Среда'),
        (TUESDAY_INDEX, 'Четверг'),
        (FRIDAY_INDEX, 'Пятница'),
        (SATURDAY_INDEX, 'Суббота'),
        (SUNDAY_INDEX, 'Воскресенье'),
    )

    index = models.PositiveIntegerField(
        default=0,
        verbose_name='Индекс дня',
        help_text='0 - Понедельник, 6 - Воскресенье',
        choices=DAY_CHOICES,
    )
    start_time = models.TimeField(verbose_name='Время начала стирки в этот день')
    end_time = models.TimeField(verbose_name='Время конца стирки в этот день')

    class Meta:
        verbose_name = 'День для стрики'
        verbose_name_plural = 'Дни для стирки'

    def __str__(self) -> str:
        return f'{self.DAY_CHOICES[self.index][1]} {self.start_time} - {self.end_time}'


class Settings(models.Model):
    days = models.ManyToManyField(
        Day,
        related_name='settings',
        verbose_name='Дни для стирки',
    )
    wash_duration = models.DurationField(verbose_name='Время стирки для одной ячейки')

    class Meta:
        verbose_name = 'Настройка'
        verbose_name_plural = 'Настройка'

    def __str__(self) -> str:
        return self.Meta.verbose_name


class Cell(models.Model):
    user = models.ForeignKey(
        User,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name='Пользователь',
    )
    start_time = models.TimeField(verbose_name='Время начала стирки')
    end_time = models.TimeField(verbose_name='Время конца стирки')
    date = models.DateField(verbose_name='Дата стирки')
    is_occupied = models.BooleanField(verbose_name='Занята')

    class Meta:
        verbose_name = 'Ячейка'
        verbose_name_plural = 'Ячейки'

    def __str__(self) -> str:
        return (
            f'{self.user.username} - {self.date} - {self.start_time} - {self.end_time}'
        )
