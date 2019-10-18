from django.shortcuts import render
from django.http import HttpResponse
#from .models import Post

# Create your views here.


def index(request, template_name='employee/home.html'):
    return render(request, template_name)

def add_employee(request, template_name='employee/add_employee.html'):
    return render(request, template_name)

