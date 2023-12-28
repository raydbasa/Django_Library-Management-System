from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import EbooksViewSet, FacultyViewSet, NewsViewSet, LibraryViewSet, CategoryViewSet, SectionsViewSet, \
    CopiesViewSet, AuthorViewSet, PublisherViewSet, LanguageViewSet, DepositsViewSet, BookViewSet

router = DefaultRouter()
router.register(r'ebooks', EbooksViewSet, basename='ebooks')
router.register(r'faculty', FacultyViewSet, basename='faculty')
router.register(r'news', NewsViewSet, basename='news')
router.register(r'library', LibraryViewSet, basename='library')
router.register(r'category', CategoryViewSet, basename='category')
router.register(r'sections', SectionsViewSet, basename='sections')
router.register(r'copies', CopiesViewSet, basename='copies')
router.register(r'author', AuthorViewSet, basename='author')
router.register(r'publisher', PublisherViewSet, basename='publisher')
router.register(r'language', LanguageViewSet, basename='language')
router.register(r'deposits', DepositsViewSet, basename='deposits')
router.register(r'books', BookViewSet, basename='book')

urlpatterns = [
    path('', include(router.urls)),
]
