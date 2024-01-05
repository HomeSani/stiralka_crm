from datetime import datetime, timedelta

from django.core.management.base import BaseCommand

from schedule.models import Day, Settings, Cell


class Command(BaseCommand):
    help = "Создаёт ячейки для двух недель вперёд"

    def handle(self, *args, **options):
        current_datetime = datetime.now()
        end_datetime = current_datetime + timedelta(days=14)
        settings = Settings.objects.first()
        day_indexes = settings.days.values_list('index', flat=True)
        wash_duration = settings.wash_duration
        days_by_indexes = {}

        for day_index in day_indexes:
            days_by_indexes[day_index] = Day.objects.filter(index=day_index).first()

        while current_datetime < end_datetime:
            datetime_weekday = current_datetime.weekday()

            if datetime_weekday in day_indexes:
                day = days_by_indexes.get(datetime_weekday)
                day_start_time = day.start_time
                day_start_datetime = datetime.combine(current_datetime, day_start_time)
                day_end_time = day.end_time
                day_end_datetime = datetime.combine(current_datetime, day_end_time)

                print(f'Create cell for {current_datetime}')

                while day_start_datetime < day_end_datetime:

                    Cell.objects.create(
                        user=None,
                        start_time=day_start_datetime.time(),
                        end_time=(day_start_datetime + wash_duration).time(),
                        date=current_datetime,
                        is_occupied=False,
                    )

                    print(f'Created cell = Date: {current_datetime}; Time: {day_start_datetime.time()} - {(day_start_datetime + wash_duration).time()}')

                    day_start_datetime += wash_duration

            current_datetime += timedelta(days=1)
