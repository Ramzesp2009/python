from django.shortcuts import render
from rest_framework import generics
from api.models import Student
from api.serializers import StudentAPISerializer


class StudentAPIView(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentAPISerializer