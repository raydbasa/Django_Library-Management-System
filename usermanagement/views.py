from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import viewsets, status
from rest_framework.generics import CreateAPIView, UpdateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated, DjangoModelPermissionsOrAnonReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Gender, Role, Semester, Faculty, City, ChangePasswordToken, UserProfile
from .serializers import GenderSerializer, RoleSerializer, SemesterSerializer, FacultySerializer, CitySerializer, \
    SignupSerializer
from .utils import send_reset_password_email

User = get_user_model()


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
    queryset = UserProfile.objects.all()
    serializer_class = SignupSerializer
    permission_classes = [AllowAny]


class LogoutAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SendForgotPasswordAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        user = None
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return Response(data=None, status=404)

        token = ChangePasswordToken.objects.create(user=user)
        redirect_url = request.build_absolute_uri(
            f'{reverse("usermanagement:reset_forget_password_api_view")}?token_id={token.pk}?user_id={user.pk}'
        )
        send_reset_password_email(user.profile.email, redirect_url)
        return Response(data=None, status=201)


class ResetForgotPasswordAPIView(APIView):
    permission_classes = [AllowAny]

    def put(self, request, *args, **kwargs):
        token_id = request.data.get('token_id')
        user_id = request.data.get('user_id')
        password = request.data.get('new_password')
        password_confirm = request.data.get('new_password2')
        if password != password_confirm:
            return Response(
                data={'password': ['Passwords do not match']},
                status=status.HTTP_400_BAD_REQUEST
            )
        try:
            token = ChangePasswordToken.objects.get(pk=token_id)
            user = User.objects.get(pk=user_id)
        except (ChangePasswordToken.DoesNotExist, User.DoesNotExist):
            return Response(data=None, status=404)
        user.set_password(password)
        user.save()
        token.delete()
        return Response(data=None, status=201)


class ResetPasswordAPIView(UpdateAPIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, *args, **kwargs):
        user = request.user
        old_password = request.data.get('old_password')
        new_password = request.data.get('new_password')
        new_password_confirm = request.data.get('new_password2')
        if new_password != new_password_confirm:
            return Response(
                data={'password': ['Passwords do not match']},
                status=status.HTTP_400_BAD_REQUEST
            )
        if not user.check_password(old_password):
            return Response(
                data={'old_password': ['Wrong password']},
                status=status.HTTP_400_BAD_REQUEST
            )
        user.set_password(new_password)
        user.save()
        return Response(data=None, status=status.HTTP_200_OK)
