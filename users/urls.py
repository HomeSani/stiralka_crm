from django.urls import path

from users.views import RegisterByTelegramView

urlpatterns = [
    path(
        'register_by_tg/',
        RegisterByTelegramView.as_view(),
        name='register_by_telegram',
    )
]
