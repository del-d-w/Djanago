from django.urls import path, re_path
from EmployeeApp import views


urlpatterns = [
    path('department', views.departmentApi),
    re_path(r'^department/(?P<id>\d+)$', views.departmentApi),
    path('employee', views.employeeApi),
    re_path(r'^employee/(?P<id>\d+)$', views.employeeApi),
]