from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse
from rest_framework import status, viewsets, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response

from authen.models import Profiles
from authen.seriazlizers import ProfileSerializer
from authen.services.ad import GetDataFromAD
from authen.services.base_auth import AuthBackend
from authen.services.tokens import JWTToken


@api_view(['GET'])
def check_auth(request):
    """Проверка авторизации пользователя"""
    auth = AuthBackend()
    data = auth.authenticate(request=request)
    if data is not None:
        return Response(status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_401_UNAUTHORIZED)


@api_view(['GET'])
@login_required
def check_admin(request):
    """Проверка пользователя на права администратора"""
    if request.user.is_superuser:
        return JsonResponse({'is_admin': True})
    else:
        return JsonResponse({'is_admin': False})


@api_view(['POST'])
def auth_login(request):
    """Авторизация пользователя"""
    try:
        data_login = request.data.get('login')
    except BaseException:
        return JsonResponse({'error': 'Имя пользователя не было предоставлено'})
    user = authenticate(request, username=data_login, password=request.data.get('pass'))
    if user is not None:
        ad_data = GetDataFromAD(request.data.get('login'))
        fio_list = ad_data[0][0].split(' ')
        if Profiles.objects.filter(djuser__in=User.objects.filter(username=request.data.get('login'))).exists():
            prof = Profiles.objects.get(djuser_id=User.objects.get(username=request.data.get('login')).id)
        else:
            new_profile = Profiles()
            new_profile.djuser_id = user.id
            new_profile.surname = fio_list[0]
            new_profile.name = fio_list[1]
            if len(fio_list) == 3:
                new_profile.patronymic = fio_list[2]
            print(ad_data[1])
            if len(ad_data[1]) > 0:
                new_profile.phone = ad_data[1][0]
            if ad_data[2][0]:
                new_profile.department = ad_data[2][0]
            if ad_data[3][0]:
                new_profile.position = ad_data[3][0]
            prof = new_profile.save()
        auth_data = JWTToken(user.id)
        dict_res = {}
        dict_res['token'] = auth_data['access_token']
        dict_res['profile_id'] = prof.id
        if len(fio_list) == 3:
            dict_res['fio'] = f'{fio_list[0]} {fio_list[1]} {fio_list[2]}'
        else:
            dict_res['fio'] = f'{fio_list[0]} {fio_list[1]}'
        return JsonResponse(dict_res)
    else:
        return JsonResponse({'error': 'Неправильный логин или пароль. Повторите попытку'})


class ProfileInfoViewSet(viewsets.ReadOnlyModelViewSet):
    """Получение информации о пользователе"""
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ProfileSerializer
    queryset = Profiles.objects.all()

    def get_info(self, request):
        profile = self.queryset.get(djuser_id=request.user.id)
        try:
            serialize = self.serializer_class(profile)
            return JsonResponse({
                'profile': serialize.data,
                'email': request.user.email
            })
        except BaseException:
            return Response(status=status.HTTP_400_BAD_REQUEST)
