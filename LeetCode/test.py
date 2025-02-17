from django.shortcuts import render
from rest_framework import generics
from .models import Student
from .serializers import StudentAPISerializer
from rest_framework.permissions import IsAuthenticated

# Erstellen Sie Ihre Ansichten hier.

class StudentAPIView(generics.ListAPIView):
    queryset = Student.objects.all()  # Abfrage aller Studenten
    serializer_class = StudentAPISerializer  # Serializer für die
    permission_classes = [IsAuthenticated]

class StudentDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentAPISerializer
    permission_classes = [IsAuthenticated]