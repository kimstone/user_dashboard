from django.shortcuts import render, redirect
from django.contrib import messages
import bcrypt

from . models import User

# Create your views here.

def dashboard_view(request):
    context = {
        'page_title': "Test App Dashboard",
        'page_meta_description': "SEO for Test App Dashboard",
    }
    return render(request, 'access_control/dashboard.html', context)



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
        return render(request, 'access_control/register-success.html', context)



def show_registration_form_view(request):
    context = {
        'page_title': "User Registration",
        'page_meta_description': "SEO for User Registration",
    }
    return render(request, 'access_control/register.html', context)