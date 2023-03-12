from django.urls import path, re_path
from EmployeeApp import views


urlpatterns = [
    path('department', views.departmentApi),
    re_path(r'^department/(?P<id>\d+)$', views.departmentApi),
    path('employee', views.employeeApi),
    re_path(r'^employee/(?P<id>\d+)$', views.employeeApi),
    path('',views.home,name='home'),
    path('create_user/', views.create_user, name='create_user'),
    path('update_employee/<int:id>/', views.update_employee,  name='update_employee'),
    path('delete_employee/<int:id>/', views.delete_employee, name='delete_employee'),


]