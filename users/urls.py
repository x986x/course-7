from django.urls import path
from rest_framework_simplejwt.views import token_obtain_pair, token_refresh

from users import views
from users.apps import UsersConfig

app_name = UsersConfig.name

urlpatterns = [
    path("token/obtain/", token_obtain_pair, name="token-obtain-pair"),
    path("token/refresh/", token_refresh, name="token-refresh"),
    path("registration/", views.RegistrationAPIVIew.as_view(), name="registration"),
]
