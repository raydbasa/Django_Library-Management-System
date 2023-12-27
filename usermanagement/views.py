from rest_framework import viewsets, status
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated, DjangoModelPermissionsOrAnonReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Gender, Role, Semester, Faculty, City
from .serializers import GenderSerializer, RoleSerializer, SemesterSerializer, FacultySerializer, CitySerializer, \
    SignupSerializer


class GenderViewSet(viewsets.ModelViewSet):
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    queryset = Gender.objects.all()
    serializer_class = GenderSerializer


class RoleViewSet(viewsets.ModelViewSet):
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    queryset = Role.objects.all()
    serializer_class = RoleSerializer


class SemesterViewSet(viewsets.ModelViewSet):
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    queryset = Semester.objects.all()
    serializer_class = SemesterSerializer


class FacultyViewSet(viewsets.ModelViewSet):
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    queryset = Faculty.objects.all()
    serializer_class = FacultySerializer


class CityViewSet(viewsets.ModelViewSet):
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    queryset = City.objects.all()
    serializer_class = CitySerializer


class SignupAPIView(CreateAPIView):
    serializer_class = SignupSerializer
    permission_classes = [AllowAny]


class LogoutAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
