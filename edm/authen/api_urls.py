from django.urls import path

from authen.api_views import check_auth, auth_login, ProfileInfoViewSet, check_admin

urlpatterns = [
    path('check_auth/', check_auth, name="check_auth"),
    path('check_admin/', check_admin, name="check_admin"),
    path('login/', auth_login, name="auth_login"),
    path('profile/', ProfileInfoViewSet.as_view({'get': 'get_info'}))
]