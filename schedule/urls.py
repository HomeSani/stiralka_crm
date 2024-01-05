from django.urls import path

from schedule.views import ScheduleView

urlpatterns = [path('', ScheduleView.as_view(), name='schedule')]
