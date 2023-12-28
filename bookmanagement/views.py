from rest_framework import viewsets

from .models import Ebooks, Faculty, News, Library, Category, Sections, Copies, Author, Publisher, Language, Deposit,Book
from .serializers import EbooksSerializer, FacultiesSerializer, NewsSerializer, LibrarySerializer, CategorySerializer, \
    SectionsSerializer, CopiesSerializer, AuthorSerializer, PublisherSerializer, LanguageSerializer, DepositSerializer, BookSerializer


class EbooksViewSet(viewsets.ModelViewSet):
    queryset = Ebooks.objects.all()
    serializer_class = EbooksSerializer


class FacultyViewSet(viewsets.ModelViewSet):
    queryset = Faculty.objects.all()
    serializer_class = FacultiesSerializer


class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer


class LibraryViewSet(viewsets.ModelViewSet):
    queryset = Library.objects.all()
    serializer_class = LibrarySerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class SectionsViewSet(viewsets.ModelViewSet):
    queryset = Sections.objects.all()
    serializer_class = SectionsSerializer


class CopiesViewSet(viewsets.ModelViewSet):
    queryset = Copies.objects.all()
    serializer_class = CopiesSerializer


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class PublisherViewSet(viewsets.ModelViewSet):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer


class LanguageViewSet(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer


class DepositsViewSet(viewsets.ModelViewSet):
    queryset = Deposit.objects.all()
    serializer_class = DepositSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

