from rest_framework import serializers

from authen.models import Profiles


class ProfileSerializer(serializers.ModelSerializer):
    """Сериализация модели профиля пользователя"""
    class Meta:
        model = Profiles
        fields = '__all__'