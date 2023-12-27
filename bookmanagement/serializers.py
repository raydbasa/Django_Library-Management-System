from rest_framework import serializers
from .models import Gender, Role, Semester, Faculty, City, CustomUser


class GenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gender
        fields = ['gender_name']


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ['role_name']


class SemesterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Semester
        fields = ['semester_name']


class FacultySerializer(serializers.ModelSerializer):
    class Meta:
        model = Faculty
        fields = ['faculty_name']


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['city_name']


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'password', 'email', 'role', 'semester', 'faculty', 'city', 'gender']
        extra_kwargs = {
            'password': {'write_only': True},
        }
