from django.urls import path

from schedule.views import MainView

urlpatterns = [
    path('', MainView.as_view(), name='main_schedule'),
]
