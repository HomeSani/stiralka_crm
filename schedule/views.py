from datetime import datetime

from django.http import HttpRequest
from django.shortcuts import render
from django.views import View

from schedule.utils import get_schedule_on_week


class MainView(View):
    """Main view for schedule"""

    def get(self, request: HttpRequest):
        """Get method"""
        week_id = request.GET.get('week_id')
        schedule = get_schedule_on_week(week_id)

        for day, cells in schedule.items():
            for cell in cells:
                cell['time_start'] = datetime(
                    2021,
                    1,
                    1,
                    int(cell['time_start'].seconds / 3600),
                    int(cell['time_start'].seconds % 3600),
                )
                cell['time_end'] = datetime(
                    2021,
                    1,
                    1,
                    int(cell['time_end'].seconds / 3600),
                    int(cell['time_end'].seconds % 3600),
                )

        context = {
            'schedule': schedule,
        }

        return render(request, 'main.html', context)
