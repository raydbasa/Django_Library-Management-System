from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

User = get_user_model()


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Publisher(models.Model):
    publisher = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.publisher} {self.location}"


class Faculty(models.Model):
    id = models.AutoField(primary_key=True)
    faculty = models.CharField(max_length=50)
    faculty_persian = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.faculty} - {self.faculty_persian}"


class Book(models.Model):
    id = models.AutoField(primary_key=True)
    signatory = models.CharField(max_length=100)
    title = models.CharField(max_length=255)
    isbn = models.CharField(max_length=30)
    pages = models.IntegerField()
    language = models.IntegerField()
    edition = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    publication = models.IntegerField(validators=[MinValueValidator(1000), MaxValueValidator(9999)])
    section = models.IntegerField()
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return self.title


class Ebooks(models.Model):
    id = models.AutoField(primary_key=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, null=True)
    extension = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.book.title} - {self.extension}"

    def save(self, *args, **kwargs):
        # Set a default book ID if none is provided
        if not self.book_id:
            default_book = Book.objects.first()  # Replace with your logic to get the default book
            self.book = default_book
        super().save(*args, **kwargs)


class News(models.Model):
    id = models.AutoField(primary_key=True)
    news_title = models.CharField(max_length=255)
    news_summary = models.TextField()
    news_details = models.TextField()
    news_ref = models.CharField(max_length=255)
    news_title_persian = models.CharField(max_length=255)
    news_summary_persian = models.TextField()
    news_details_persian = models.TextField()
    news_ref_persian = models.CharField(max_length=255)
    news_date = models.DateTimeField()
    fileext = models.CharField(max_length=3)
    faculties_id = models.IntegerField()

    def __str__(self):
        return f"{self.news_title} - {self.news_date}"


class Library(models.Model):
    id = models.AutoField(primary_key=True)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, null=True)
    content = models.TextField()
    content_persian = models.TextField()
    privacy = models.TextField()
    privacy_persian = models.TextField()
    services = models.TextField()
    services_persian = models.TextField()
    email = models.EmailField(max_length=250)

    def __str__(self):
        return str(self.id)


class Category(models.Model):
    name = models.CharField(max_length=100)
    name_persian = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Sections(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    section = models.CharField(max_length=100)
    section_persian = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.section} - {self.section_persian}"


class Copies(models.Model):
    STATUS_CHOICES = [
        ('Available', 'Available'),
        ('Checked Out', 'Checked Out'),
    ]

    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Available')

    def __str__(self):
        return f"{self.book.title} - {self.status}"


class Language(models.Model):
    language = models.CharField(max_length=70)

    def __str__(self):
        return self.language


class Deposit(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    copy = models.ForeignKey(Copies, on_delete=models.CASCADE)
    issue_date = models.DateField()
    due_date = models.DateField()

    def __str__(self):
        return f"Deposit {self.id} by {self.user.username} - {self.copy.book.title}"
