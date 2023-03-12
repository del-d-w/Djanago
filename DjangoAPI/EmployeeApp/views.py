from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from EmployeeApp.models import Departments,Employees
from EmployeeApp.serializers import DepartmentsSerializer, EmployeesSerializer

# Create your views here.

@csrf_exempt
def departmentApi(request, id=0):
    if request.method == 'GET':
        if id:
            try:
                department = Departments.objects.get(DepartmentId=id)
                department_serializer = DepartmentsSerializer(department)
                return JsonResponse(department_serializer.data, safe=False)
            except Departments.DoesNotExist:
                return JsonResponse(f"Department with ID {id} does not exist.", safe=False)
        else:
            departments = Departments.objects.all()
            departments_serializer = DepartmentsSerializer(departments, many=True)
            return JsonResponse(departments_serializer.data, safe=False)
    elif request.method == 'POST':
        # Handle POST request for Departments
        department_data = JSONParser().parse(request)
        departments_serializer = DepartmentsSerializer(data=department_data)
        if departments_serializer.is_valid():
            departments_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method == 'PUT':
        # Handle PUT request for Departments
        department_data = JSONParser().parse(request)
        department = Departments.objects.get(DepartmentId=id)
        departments_serializer = DepartmentsSerializer(department, data=department_data)
        if departments_serializer.is_valid():
            departments_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update", safe=False)
    elif request.method == 'DELETE':
        # Handle DELETE request for Departments
        department = Departments.objects.get(DepartmentId=id)
        department.delete()
        return JsonResponse("Deleted Successfully", safe=False)

@csrf_exempt
def employeeApi(request, id=0):
    if request.method == 'GET':
        if id:
            try:
                employee = Employees.objects.get(EmployeeId=id)
                employee_serializer = EmployeesSerializer(employee)
                return JsonResponse(employee_serializer.data, safe=False)
            except Employees.DoesNotExist:
                return JsonResponse(f"Employee with ID {id} does not exist.", safe=False)
        else:
            employees = Employees.objects.all()
            employees_serializer = EmployeesSerializer(employees, many=True)
            return JsonResponse(employees_serializer.data, safe=False)
    elif request.method == 'POST':
        # Handle POST request for Departments
        employee_data = JSONParser().parse(request)
        employees_serializer = EmployeesSerializer(data=employee_data)
        if employees_serializer.is_valid():
            employees_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method == 'PUT':
        # Handle PUT request for Departments
        employee_data = JSONParser().parse(request)
        employee = Employees.objects.get(EmployeeId=id)
        employee_serializer = EmployeesSerializer(employee, data=employee_data)
        if employee_serializer.is_valid():
            employee_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update", safe=False)
    elif request.method == 'DELETE':
        # Handle DELETE request for Departments
        employee = Employees.objects.get(EmployeeId=id)
        employee.delete()
        return JsonResponse("Deleted Successfully", safe=False)
