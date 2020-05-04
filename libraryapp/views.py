from django.core.mail import send_mail
from django.http import BadHeaderError
from django.shortcuts import HttpResponse, render, HttpResponseRedirect, get_object_or_404, get_list_or_404, Http404

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .models import *
from .forms import *


@login_required(login_url='/login')
def index(request):
    return HttpResponseRedirect('/clients/')

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(
                request=request,
                username=username,
                password=password
            )

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/')
            else:
                return HttpResponse('Invalid login or password')
    else:
        form = LoginForm()
    return render(request,
                  'login-page.html',
                  context={'form': form})

@login_required(login_url='/login')
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login')

@login_required(login_url='/login')
def client_list(request):
    library = LibraryEmployee.objects.get(id=request.user.id).library
    clients = Client.objects.all()

    return render(request,
                  'client/list.html',
                  context={ 'library':library, 'clients':clients })

@login_required(login_url='/login')
def client_add(request):
    library = LibraryEmployee.objects.get(id=request.user.id).library

    if request.method == "POST":
        clientForm = ClientForm(request.POST)
        if clientForm.is_valid():
            clientForm.save()
    else:
        clientForm = ClientForm()

    return render(request,
                  'client/add.html',
                  context={ 'library':library, 'clientForm':clientForm })

@login_required(login_url='/login')
def client_edit(request, pk):
    library = LibraryEmployee.objects.get(id=request.user.id).library
    client = get_object_or_404(Client, id = pk)

    if request.method == "POST":
        clientForm = ClientForm(request.POST)
        if clientForm.is_valid():
            clientForm.save()
    else:
        clientForm = ClientForm(instance=client)

    return render(request,
                  'client/edit.html',
                  context={'library': library, 'clientForm': clientForm})

@login_required(login_url='/login')
def client_delete(request, pk):
    client = get_object_or_404(Client, id = pk)
    Client.delete(client)
    return HttpResponseRedirect('/clients/')

@login_required(login_url='/login')
def client_details(request, pk):
    library = LibraryEmployee.objects.get(id=request.user.id).library
    client = get_object_or_404(Client, id = pk)
    card_items = CardItem.objects.filter(client_id=client.id)

    return render(request,
                  'client/details.html',
                  context={ 'client': client, 'card_items': card_items, 'library': library })

@login_required(login_url='/login')
def client_fine(request, pk, fine):
    library = LibraryEmployee.objects.get(id=request.user.id).library
    client = get_object_or_404(Client, id = pk)
    client.fine += fine
    client.save()

    subject = "У вас появилась задолжность! " + str(library)
    message = "Вы не вернули книгу, поэтому вам начислена задолжность в размере " + str(fine) + '\n аша общая задолжность: ' + str(client.fine)
    destination_mail = [client.email, ]

    try:
        send_mail(subject, message, 'noreply@nebezdari.ru', destination_mail)
    except BadHeaderError:
        return HttpResponse('Invalid header found')

    return HttpResponseRedirect('/client/' + str(pk) + '/details/')

@login_required(login_url='/login')
def extend(request, pk):
    card_item = get_object_or_404(CardItem, id = pk)
    card_item.returned_date += timedelta(days=7)
    card_item.save()
    return HttpResponseRedirect('/client/' + str(card_item.client.id) + '/details/')

@login_required(login_url='/login')
def book_list(request):
    library = LibraryEmployee.objects.get(id=request.user.id).library
    books = Book.objects.filter(library=library)

    return render(request,
                  'book/list.html',
                  context={'library': library, 'books': books})

@login_required(login_url='/login')
def book_add(request):
    library = LibraryEmployee.objects.get(id=request.user.id).library

    if request.method == "POST":
        bookForm = BookForm(library, request.POST)
        if bookForm.is_valid():
            book = bookForm.save(commit=False)
            book.library = library
            bookForm.save()
    else:
        bookForm = BookForm(library)

    return render(request,
                  'book/add.html',
                  context={'library': library, 'bookForm': bookForm})

@login_required(login_url='/login')
def book_edit(request, pk):
    library = LibraryEmployee.objects.get(id=request.user.id).library
    book = get_object_or_404(Book, id=pk)

    if request.method == "POST":
        bookForm = BookForm(library, request.POST)
        if bookForm.is_valid():
            bookForm.save()
    else:
        bookForm = BookForm(library, instance=book)

    return render(request,
                  'book/edit.html',
                  context={'library': library, 'bookForm': bookForm})

@login_required(login_url='/login')
def book_delete(request, pk):
    book = get_object_or_404(Book, id=pk)
    Book.delete(book)
    return HttpResponseRedirect('/books/')