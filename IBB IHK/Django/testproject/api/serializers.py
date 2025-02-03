from rest_framework import serializers
from .models import Student


class StudentAPISerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = [
            'id',
            'first_name',
            'last_name',
            'age',
        ]