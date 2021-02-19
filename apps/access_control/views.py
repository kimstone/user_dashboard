from django.shortcuts import render, redirect
from django.contrib import messages

from . models import *

# Create your views here.

def dashboard(request):
    context = {
        'page_title': "Test App Dashboard",
        'page_meta_description': "SEO for Test App Dashboard",
    }
    return render(request, 'access_control/dashboard.html', context)
