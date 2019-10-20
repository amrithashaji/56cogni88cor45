from rest_framework import generics
from ..models import Employee
from employee_app.employee_api.serializers import EmployeeSerializer
from django.shortcuts import render
from django.http import JsonResponse


class allEmployees(generics.ListCreateAPIView):
    """ Employee List View """
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class  detailsapi(generics.ListCreateAPIView):
    """ Employee details View """

    def get(self, request, pk):
        employe =  list(Employee.objects.filter(pk=pk).values())
        data =  dict()
        data['employe'] = employe
        return JsonResponse(data)
        
