from rest_framework import serializers

from .models import *


class EbooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ebooks
        fields = ['id', 'book_id', 'extension']


class FacultiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Faculty
        fields = ['id', 'faculty', 'faculty_persian']


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ['id', 'news_title', 'news_summary', 'news_details', 'news_ref', 'news_title_persian',
                  'news_summary_persian', 'news_details_persian', 'news_ref_persian', 'news_date', 'fileext',
                  'faculties_id']


class LibrarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Library
        fields = ['id', 'faculty_id', 'content', 'content_persian', 'privacy', 'privacy_persian',
                  'services', 'services_persian', 'email']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'name_persian']


class SectionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sections
        fields = ['sections', 'sections']


class CopiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Copies
        fields = ['id', 'book', 'status']


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = [' first_name', 'last_name']


class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = ['publisher', 'location']


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ['language']


class DepositSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deposit
        fields = ['id', 'user', 'copy', 'issue_date', 'due_date']


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = [
            'id', 'signatory', 'title', 'isbn','pages','language','edition','author','publisher',
            'publication','section','faculty','description',
        ]

