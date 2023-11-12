import datetime
from datetime import timedelta

from schedule.models import Settings, Talon


def get_schedule() -> dict:
    """Get blank schedule by week"""
    settings = Settings.objects.first()
    days = settings.available_days.all()
    wash_duration = timedelta(hours=settings.wash_duration)
    weeks_count = datetime.date(year=2023, month=12, day=28).isocalendar()[1]
    schedule = {}

    for week_number in range(1, weeks_count + 1):
        schedule[week_number] = {}

        for day in days:
            time_start = timedelta(hours=day.worktime_start.hour)
            time_end = timedelta(hours=day.worktime_end.hour)
            cells = []

            while time_start < time_end:
                cells.append(
                    {
                        'time_start': time_start,
                        'time_end': time_start + wash_duration,
                        'is_available': False,
                    }
                )

                time_start += wash_duration

            schedule[week_number][day.index] = cells

    return schedule


def get_schedule_on_week(week_id: int) -> dict:
    """Get schedule on week by week_id"""
    schedule = get_schedule()
    talons = Talon.objects.filter(week_id=46)
    cells_in_week = schedule[week_id]

    for talon in talons:
        talon_time_start = timedelta(hours=talon.time_start.hour)
        talon_time_end = timedelta(hours=talon.time_end.hour)
        cells_in_day = cells_in_week[talon.day_id]

        for cell in cells_in_day:
            if (
                talon_time_start < cell['time_end']
                and talon_time_end > cell['time_start']
            ):
                cell['is_available'] = True

    return cells_in_week
