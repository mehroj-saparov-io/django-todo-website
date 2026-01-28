from django.urls import path
from .views import CustomLoginView, CustomLogoutView, register, profile, create_task, update_task, delete_task

urlpatterns = [
    path("login/", CustomLoginView.as_view(), name="login"),
    path("logout/", CustomLogoutView.as_view(), name="logout"),
    path("register/", register, name="register"),
    path("profile/", profile, name="profile"),

    path("tasks/create/", create_task, name="task_create"),
    path("tasks/<int:pk>/update/", update_task, name="task_update"),
    path("tasks/<int:pk>/delete/", delete_task, name="task_delete"),

]
