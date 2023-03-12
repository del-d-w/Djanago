from rest_framework import serializers
from EmployeeApp.views import Departments,Employees

class DepartmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Departments
        fields=('DepartmentId','DepartmentName')

class EmployeesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employees
        fields=('EmployeeId','EmployeeName','Department','DateOfJoining','photo')