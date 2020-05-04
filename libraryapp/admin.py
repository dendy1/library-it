from django.contrib import admin

from .models import *

admin.site.register(Library)
admin.site.register(Book)
admin.site.register(Client)
admin.site.register(CardItem)
admin.site.register(LibraryEmployee)
admin.site.register(Author)