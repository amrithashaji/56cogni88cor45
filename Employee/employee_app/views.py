from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Employee
import requests
import json


# Create your views here.

def index(request, template_name='employee/home.html'):
    return render(request, template_name)

def ajaxHome(request):
    url='http://localhost:9000/allEmployees'
    response = requests.get(url)
    geodata = response.json()
    emp_list  = []
    
    if geodata:
        for each in geodata:

            emp_id = each["id"]
            emp_name = each["employee_name"]
            emp_email = each["email"]

            emp = {}

            emp["emp_id"] = emp_id
            emp["emp_name"] = emp_name
            emp["emp_email"] = emp_email
            emp_list.append(emp)   

    return HttpResponse(json.dumps(emp_list), content_type='application/json')

def employeDetails(request, empid, template_name='employee/employe_details.html'):
    return render(request, template_name, {'empid':empid})


def ajaxEmployeDetails(request):
    url='http://localhost:9000/detailsapi/'

    empid = request.GET.get('empid')
    
    emp_details = requests.get(url+empid)
    data = emp_details.json()

    detailsList = []
    detailsDict = {}

    detailsDict["id"] = data['employe'][0]['id']
    detailsDict["name"] = data['employe'][0]['employee_name']
    detailsDict["email"] = data['employe'][0]['email']
    detailsDict["password"] = data['employe'][0]['password']
    detailsDict["phone"] = data['employe'][0]['phone']
    detailsDict["address"] = data['employe'][0]['address']
    detailsDict["photo"] = data['employe'][0]['image_as_a_blob']
    detailsList.append(detailsDict)
    
    return HttpResponse(json.dumps(detailsList), content_type='application/json')


def add_employee(request, template_name='employee/add_employee.html'):

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        pswd = request.POST.get('pswd')
        ph = request.POST.get('ph')
        address = request.POST.get('addr')
        photo = request.POST.get('photo')
        
        createEmployee = Employee.objects.create(
            employee_name = name,
            image_as_a_blob = photo,
            email = email,
            password = pswd,
            phone = ph,
            address  = address
        )

        createEmployee.save()
        return redirect('/home/')
        
    return render(request, template_name)

