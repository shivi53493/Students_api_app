from django.shortcuts import render
from students_app.models import Students
from rest_framework.decorators import api_view
from .serializers import StudentSerializer,EmployeeSerializer,TeacherSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from employees_app.models import Employee
from django.http import Http404
from rest_framework import mixins,generics
from teacher_app.models import Teacher

@api_view(['GET','POST'])
def students(request):
    if request.method =="GET":
        students = Students.objects.all()
        serializer = StudentSerializer(students,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    elif request.method =="POST":
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors)

    return Response(status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET','PUT','DELETE'])
def student_details(request,pk):
    try:
        student = Students.objects.get(pk=pk)
    except Students.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        serializer = StudentSerializer(student)
        return Response(serializer.data,status=status.HTTP_200_OK)
    elif request.method =="PUT":
        serializer = StudentSerializer(student,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors)
    elif request.method == "DELETE":
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class Employees(APIView):
    def get(self,request):
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    def post(self,request):
        serializer = EmployeeSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class EmployeeDetails(APIView):
    def get_object(self,pk):
        try:
            return Employee.objects.get(pk=pk)
        except Employee.DoesNotExist:
            return Http404
    def get(self,request,pk):
        employee = self.get_object(pk)
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data,status=status.HTTP_200_OK)
    def put(self,request,pk):
        employee = self.get_object(pk)
        serializer = EmployeeSerializer(employee,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.errors,status= status.HTTP_400_BAD_REQUEST)
    def delete(self,request,pk):
        employee = self.get_object(pk)
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class Teachers(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    def get(self,request):
        return self.list(request)
    def post(self,request):
        return self.create(request)


class TeachersDetails(generics.GenericAPIView,mixins.UpdateModelMixin,mixins.RetrieveModelMixin,mixins.DestroyModelMixin):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    def get(self,request,pk):
        return self.retrieve(request,pk)
    def put(self,request,pk):
        return self.update(request,pk)
    def delete(self,request,pk):
        return self.destroy(request,pk)
