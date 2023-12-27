from django.urls import include, path
from rest_framework import routers
from .views import GenderViewSet, RoleViewSet, SemesterViewSet, FacultyViewSet, CityViewSet, CustomUserViewSet

router = routers.DefaultRouter()
router.register(r'genders', GenderViewSet, basename='gender')
router.register(r'roles', RoleViewSet, basename='role')
router.register(r'semesters', SemesterViewSet, basename='semester')
router.register(r'faculties', FacultyViewSet, basename='faculty')
router.register(r'cities', CityViewSet, basename='city')
router.register(r'customusers', CustomUserViewSet, basename='customuser')

urlpatterns = [
    path('', include(router.urls)),
]
