import json

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views import View

from schedule.models import Cell, Day


class ScheduleView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        cells = Cell.objects.all()
        schedule = {}

        for cell in cells:
            week_day_index = cell.date.weekday()
            day_name = Day.DAY_CHOICES[week_day_index][1]

            old_cells = schedule.get(day_name)

            if old_cells is None:
                schedule[day_name] = [cell]
                continue

            old_cells.append(cell)
            schedule[day_name] = old_cells

        context = {
            'schedule': schedule,
        }

        return render(request, 'schedule.html', context)

    def post(self, request: HttpRequest) -> HttpResponse:
        json_data = json.loads(request.body)
        cell_id = json_data.get('cell_id')

        if cell_id is None:
            return HttpResponse(status=400)

        cell = Cell.objects.filter(id=cell_id).first()

        if cell is None:
            return HttpResponse(status=400)

        cell.user = request.user
        cell.is_occupied = True
        cell.save()

        return HttpResponse(status=200)
