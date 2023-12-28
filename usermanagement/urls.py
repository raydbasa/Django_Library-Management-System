from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

from .views import GenderViewSet, RoleViewSet, SemesterViewSet, FacultyViewSet, CityViewSet, SignupAPIView, \
    LogoutAPIView, ResetPasswordAPIView, SendForgotPasswordAPIView, \
    ResetForgotPasswordAPIView

app_name = 'usermanagement'
router = routers.DefaultRouter()
router.register(r'genders', GenderViewSet, basename='gender')
router.register(r'roles', RoleViewSet, basename='role')
router.register(r'semesters', SemesterViewSet, basename='semester')
router.register(r'faculties', FacultyViewSet, basename='faculty')
router.register(r'cities', CityViewSet, basename='city')

urlpatterns = [
    path('', include(router.urls)),
    path('signup/', SignupAPIView.as_view(), name='signup_api_view'),
    path('login/', obtain_auth_token, name='login_api_view'),
    path('logout/', LogoutAPIView.as_view(), name='logout_api_view'),
    path('reset-password/', ResetPasswordAPIView.as_view(), name='reset_password_api_view'),
    path('send-forget-password/', SendForgotPasswordAPIView.as_view(), name='send_forget_password_api_view'),
    path('reset-forget-password/', ResetForgotPasswordAPIView.as_view(), name='reset_forget_password_api_view'),

]
