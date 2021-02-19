from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard_view, name="access_control/dashboard"),
    path('register/', views.show_registration_form_view, name="access_control/register"),
    path('register-me/', views.process_new_user_view, name="access_control/process_new_user"),
]