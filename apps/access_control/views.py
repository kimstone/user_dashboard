from django.shortcuts import render, redirect
from django.contrib import messages
import bcrypt

from . models import User

# Create your views here.

def admin_dashboard_view(request):
    context = {
        'page_title': "Admin Dashboard",
        'page_meta_description': "SEO for Admin Dashboard",
    }
    return render(request, 'access_control/dashboard-admin.html', context)



def dashboard_view(request):
    context = {
        'page_title': "Test App Dashboard",
        'page_meta_description': "SEO for Test App Dashboard",
    }
    return render(request, 'access_control/dashboard.html', context)



def authenticate_user_view(request):

    if request.method == "GET":
        return redirect('/')

    if not User.objects.authenticate_credentials(request.POST['email_add'], request.POST['password']):
        messages.error(request, 'You have entered an invalid email/password combo')
        return redirect('access_control/login_form')
    else:
        registered_user = User.objects.get(email=request.POST['email_add'])
        request.session['user_id'] = registered_user.id
        request.session['success_msg'] = "You have successfully logged in!"

        if registered_user.user_level != 9:
            return redirect('access_control/user_directory')
        else:
            return redirect('access_control/dashboard-admin')



def process_new_user_view(request):

    if request.method == "GET":
        return redirect('/')

    #errors = {}
    errors = User.objects.validate_registration_form(request.POST)

    if len(errors) > 0:

        for key, value in errors.items():
            messages.error(request, value, extra_tags='register')

        return redirect('access_control/register')
    else:
        new_user = User.objects.register_new_user(request.POST)
        context = {
            'page_title': "User Registration Success",
            'page_meta_description': "SEO for User Registration Success",
        }
        #return render(request, 'access_control/register-success.html', context)
        return redirect('access_control/login_form')



def show_login_form_view(request):
    context = {
        'page_title': "User Login Form",
        'page_meta_description': "SEO for User Login Form",
    }
    return render(request, 'access_control/login.html', context)



def show_registration_form_view(request):
    context = {
        'page_title': "User Registration",
        'page_meta_description': "SEO for User Registration",
    }
    return render(request, 'access_control/register.html', context)


def user_directory_view(request):
    context = {
        'page_title': "User Directory Dashboard",
        'page_meta_description': "SEO for User Directory Dashboard",
    }
    return render(request, 'access_control/user-directory.html', context)