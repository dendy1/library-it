from django.contrib.auth.models import AbstractUser
from django.db import models

class Library(models.Model):
    name = models.CharField(max_length=64)
    address = models.CharField(max_length=128)

class Author(models.Model):
    name = models.CharField(max_length=128)

class Book(models.Model):
    isbn = models.CharField(max_length=128)
    title = models.CharField(max_length=64)
    publication_date = models.DateField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

class LibraryEmployee(AbstractUser):
    library = models.ForeignKey(Library, null=True, on_delete=models.SET_NULL)

class Client(models.Model):
    name = models.CharField(max_length=64)
    date_of_birth = models.DateField()
    fine = models.IntegerField()

class CardItem(models.Model):
    book = models.ForeignKey(Book, null=True, on_delete=models.SET_NULL)
    given_date = models.DateTimeField()
    returned_date = models.DateTimeField()
    registry_employee = models.ForeignKey(LibraryEmployee, null=True, on_delete=models.SET_NULL)
    status = models.CharField(max_length=64)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)