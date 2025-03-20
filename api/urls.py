from django.urls import path
from . import views
from .views import Employees,EmployeeDetails
urlpatterns = [
    path('students/',views.students,name='students'),
    path('students/<int:pk>/',views.student_details,name='student_details'),

    path('employees/',Employees.as_view(),name='employees'),
    path('employees/<int:pk>/',EmployeeDetails.as_view(),name='EmployeeDetails'),
    
]
