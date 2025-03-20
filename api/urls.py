from django.urls import path
from . import views
from .views import Employees,EmployeeDetails,Teachers,TeachersDetails
urlpatterns = [
    path('students/',views.students,name='students'),
    path('students/<int:pk>/',views.student_details,name='student_details'),

    path('employees/',Employees.as_view(),name='employees'),
    path('employees/<int:pk>/',EmployeeDetails.as_view(),name='EmployeeDetails'),
    
    path('teachers/',Teachers.as_view(),name='employees'),
    path('teachers/<int:pk>/',TeachersDetails.as_view(),name='TeachersDetails'),
]
