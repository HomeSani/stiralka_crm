from rest_framework import serializers

from users.models import User


class TelegramRegisterSerializer(serializers.Serializer):
    telegram_username = serializers.CharField(max_length=255, required=True)
    telegram_uuid = serializers.CharField(max_length=255, required=True)
    telegram_name = serializers.CharField(max_length=255)

    def validate(self, data):
        user = User.objects.filter(telegram_uuid=data['telegram_uuid']).first()

        if user:
            raise serializers.ValidationError('User already exists')

        return data
