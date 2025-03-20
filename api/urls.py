from django.urls import path
from . import views
urlpatterns = [
    path('students/',views.students,name='students'),
    path('students/<int:pk>/',views.student_details,name='student_details'),
    
]
