from django.contrib.auth.models import User
from django.db import models


class Profiles(models.Model):
    """Модель профилей пользователей"""
    djuser = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        verbose_name='djuser'
    )
    surname = models.CharField(
        max_length=250,
        verbose_name='Фамилия'
    )
    name = models.CharField(
        max_length=250,
        verbose_name='Имя'
    )
    patronymic = models.CharField(
        max_length=250,
        verbose_name='Отчество'
    )
    phone = models.PositiveIntegerField(
        null=True,
        verbose_name='Номер телефона'
    )
    department = models.CharField(
        max_length=1000,
        default='',
        null=True,
        verbose_name='Подразделение'
    )
    position = models.CharField(
        max_length=250,
        default='',
        null=True,
        verbose_name='Должность'
    )

    def __str__(self):
        return f'{self.surname} {self.name} {self.patronymic}'

    class Meta:
        verbose_name = 'Профиль пользователя'
        verbose_name_plural = 'Профили пользователей'

