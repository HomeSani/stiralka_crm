from django.http import HttpRequest, HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView

from users.models import User
from users.serializers import TelegramRegisterSerializer


class RegisterByTelegramView(APIView):
    def post(self, request: HttpRequest) -> HttpResponse:
        serializer = TelegramRegisterSerializer(data=request.data)

        if serializer.is_valid():
            User.objects.create_user(
                username=serializer.validated_data.get('telegram_username'),
                telegram_uuid=serializer.validated_data.get('telegram_uuid'),
                first_name=serializer.validated_data.get('telegram_name'),
            )

            return HttpResponse(status=200)

        return Response(serializer.errors, status=400)
