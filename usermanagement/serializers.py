from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import Gender, Role, Semester, Faculty, City, UserProfile

User = get_user_model()


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


class SignupSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username')
    password = serializers.CharField(source='user.password', write_only=True)

    class Meta:
        model = UserProfile
        fields = (
            'username', 'password', 'email', 'first_name', 'last_name', 'role', 'semester', 'gender', 'faculty', 'city')
        extra_kwargs = {
            'password': {'write_only': True},
            'id': {'read_only': True}
        }

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create_user(username=user_data['username'],
                                        password=user_data['password'])
        profile = UserProfile.objects.create(user=user, **validated_data)
        return profile
