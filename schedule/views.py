import json

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views import View

from schedule.models import Cell
from users.models import User


class ScheduleView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        cells = Cell.objects.all()
        schedule = {}

        for cell in cells:
            date_str = cell.date.strftime("%m-%d-%Y")

            old_cells = schedule.get(date_str)

            if old_cells is None:
                schedule[date_str] = [cell]
                continue

            old_cells.append(cell)
            schedule[date_str] = old_cells

        context = {
            'schedule': schedule,
        }

        return render(request, 'schedule.html', context)

    def post(self, request: HttpRequest) -> HttpResponse:
        json_data = json.loads(request.body)
        cell_id = json_data.get('cell_id')
        user: User = request.user

        if cell_id is None:
            return HttpResponse(status=400)

        cell = Cell.objects.filter(id=cell_id).first()

        if cell is None:
            return HttpResponse(status=400)

        if user.restriction_on_use_count <= 0:
            return HttpResponse('restriction_on_use_count is low', status=300)

        cell.user = request.user
        cell.is_occupied = True
        cell.save()

        user.restriction_on_use_count -= 1
        user.save()

        return HttpResponse(status=200)
