from datetime import datetime, timedelta

from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models

class Library(models.Model):
    name = models.CharField(max_length=64)
    address = models.CharField(max_length=128)

    def __str__(self):
        return self.name + ' <' + self.address + '>'

class Author(models.Model):
    first_name = models.CharField(max_length=64, default='first name')
    last_name = models.CharField(max_length=64, default='last name')

    def get_full_name(self):
        return self.first_name + ' ' + self.last_name

    def __str__(self):
        return self.get_full_name()

class Book(models.Model):
    isbn = models.CharField(max_length=128)
    title = models.CharField(max_length=64)
    publication_date = models.DateField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    library = models.ForeignKey(Library, null=True, on_delete=models.CASCADE)
    cost = models.IntegerField(default=0)

    def get_full_name(self):
        return self.title + ' <' + str(self.author) + '>'

    def __str__(self):
        return self.title + ' (' + str(self.author) + ')' + '[' + str(self.library) + ']'

class LibraryEmployee(AbstractUser):
    library = models.ForeignKey(Library, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.username + ' <' + self.get_full_name() + '>'

class Client(models.Model):
    first_name = models.CharField(max_length=64, default='')
    last_name = models.CharField(max_length=64, default='')
    email = models.CharField(max_length=64, default='')
    date_of_birth = models.DateField()
    fine = models.IntegerField(default=0)
    library = models.ForeignKey(Library, null=True, on_delete=models.CASCADE)

    def current_books(self):
        books_id = CardItem.objects.values('book_id').filter(client_id=self.id)
        books = Book.objects.filter(id__in=books_id)
        return books

    def get_full_name(self):
        return self.first_name + ' ' + self.last_name

    def __str__(self):
        return self.get_full_name() + ' <' + str(self.fine) + '>'

class CardItem(models.Model):
    book = models.ForeignKey(Book, null=True, on_delete=models.SET_NULL)
    given_date = models.DateTimeField(default=datetime.now())
    returned_date = models.DateTimeField(default=datetime.now()+timedelta(days=7))
    registry_employee = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL)
    status = models.CharField(max_length=64, default="На руках")
    client = models.ForeignKey(Client, on_delete=models.CASCADE)

    def __str__(self):
        return self.book.title + ' | ' + str(self.given_date) + ' | ' + str(self.returned_date) + ' | ' + self.status + ' <' + str(self.client.get_full_name()) + '>'