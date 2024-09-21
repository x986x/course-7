from django.urls import path

from habits import views
from habits.apps import HabitsConfig

app_name = HabitsConfig.name

urlpatterns = [
    path("list/user/", views.UsersHabitListAPIView.as_view(), name="list-user"),
    path("list/public/", views.PublicHabitListAPIView.as_view(), name="list-public"),
    path("create/", views.HabitCreateAPIView.as_view(), name="create"),
    path("update/<int:pk>/", views.HabitUpdateAPIView.as_view(), name="update"),
    path("destroy/<int:pk>/", views.HabitDestroyAPIView.as_view(), name="destroy"),
]
