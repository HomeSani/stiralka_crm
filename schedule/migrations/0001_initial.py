# Generated by Django 4.2.6 on 2024-01-05 09:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Day",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "index",
                    models.PositiveIntegerField(
                        choices=[
                            (0, "Понедельник"),
                            (1, "Вторник"),
                            (2, "Среда"),
                            (3, "Четверг"),
                            (4, "Пятница"),
                            (5, "Суббота"),
                            (6, "Воскресенье"),
                        ],
                        default=0,
                        help_text="0 - Понедельник, 6 - Воскресенье",
                        verbose_name="Индекс дня",
                    ),
                ),
                (
                    "start_time",
                    models.TimeField(verbose_name="Время начала стирки в этот день"),
                ),
                (
                    "end_time",
                    models.TimeField(verbose_name="Время конца стирки в этот день"),
                ),
            ],
            options={
                "verbose_name": "День для стрики",
                "verbose_name_plural": "Дни для стирки",
            },
        ),
        migrations.CreateModel(
            name="Settings",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "wash_duration",
                    models.DurationField(
                        default="01:30:00", verbose_name="Время стирки для одной ячейки"
                    ),
                ),
                (
                    "days",
                    models.ManyToManyField(
                        related_name="settings",
                        to="schedule.day",
                        verbose_name="Дни для стирки",
                    ),
                ),
            ],
            options={
                "verbose_name": "Настройка",
                "verbose_name_plural": "Настройка",
            },
        ),
        migrations.CreateModel(
            name="Cell",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("start_time", models.TimeField(verbose_name="Время начала стирки")),
                ("end_time", models.TimeField(verbose_name="Время конца стирки")),
                ("date", models.DateField(verbose_name="Дата стирки")),
                ("is_occupied", models.BooleanField(verbose_name="Занята")),
                (
                    "user",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Пользователь",
                    ),
                ),
            ],
            options={
                "verbose_name": "Ячейка",
                "verbose_name_plural": "Ячейки",
            },
        ),
    ]