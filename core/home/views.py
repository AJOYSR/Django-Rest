from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers
from .serializers import *
from rest_framework import status
from .models import *
# Create your views here.

@api_view(["GET"])
def home(request):
    student_objs = Student.objects.all()
    serializer = StudentSerializer(student_objs, many = True) # many karon onek data aste pare tai
    return Response({'status': 200, 'payload' : serializer.data})

@api_view(["POST"])
def add_student(request):
    data = request.data
    serializer = StudentSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'status': 200, 'payload' : serializer.data, 'message': "You data send"})
    return Response({"status" : status.HTTP_403_FORBIDDEN, "message" : serializer.errors})

@api_view(["PUT"])
def update_student(request, id):
    try:
        student_obj = Student.objects.get(id = id)
        data = request.data
        serializer = StudentSerializer( student_obj ,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 200, 'payload' : serializer.data, 'message': "You data send"})
        return Response({"status" : status.HTTP_403_FORBIDDEN, "message" : serializer.errors})
    
    except Exception as e :
        return Response({'status': 403, 'message': "Invalid ID!"})


@api_view(["DELETE"])
def delete_student(request, id):
    try:
        student_obj = Student.objects.get(id = id)
        student_obj.delete()
        return Response({'status': 200, 'message': "Student Deleted"})
        
    except Exception as e :
        return Response({'status': 403, 'message': "Invalid ID!"})

