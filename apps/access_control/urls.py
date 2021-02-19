from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard_view, name="access_control/dashboard"),
    path('dashboard/admin/', views.admin_dashboard_view, name="access_control/dashboard_admin"),
    path('register/', views.show_registration_form_view, name="access_control/register"),
    path('register-me/', views.process_new_user_view, name="access_control/process_new_user"),
    path('authenticate/', views.authenticate_user_view, name="access_control/authenticate"),
    path('signin/', views.show_login_form_view, name="access_control/login_form"),
    path('users/', views.user_directory_view, name="access_control/user_directory"),
]