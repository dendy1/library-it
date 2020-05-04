from django import forms

from .models import *

class LoginForm(forms.Form):
    username = forms.CharField(
        label='Логин или E-Mail',
        widget=forms.TextInput(
            attrs={'class': 'input-1', 'placeholder': 'Введите логин или E-Mail'}
        )
    )
    password = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput(
            attrs={'class': 'input-1', 'placeholder': 'Введите пароль'}
        )
    )

class ClientForm(forms.ModelForm):
    first_name = forms.CharField(
        label='Имя клиента',
        widget=forms.TextInput(
            attrs={'class': 'input-1', 'placeholder': 'Введите имя'}
        )
    )

    last_name = forms.CharField(
        label='Фамилия клиента',
        widget=forms.TextInput(
            attrs={'class': 'input-1', 'placeholder': 'Введите фамилию'}
        )
    )

    email = forms.EmailField(
        label='E-Mail клиента',
        widget=forms.EmailInput(
            attrs={'class': 'input-1', 'placeholder': 'Введите e-mail'}
        )
    )

    date_of_birth = forms.DateField(
        label='Дата рождения клиента',
        widget=forms.DateInput(
            attrs={'class': 'datepicker-input', 'placeholder': 'Дата рождения', 'id':'datetimepicker'}
        )
    )

    fine = forms.IntegerField(
        label='Штраф',
        widget=forms.NumberInput(
            attrs={'class': 'input-1', 'placeholder': 'Введите штраф'}
        )
    )

    class Meta:
        model = Client
        fields = ('first_name', 'last_name', 'date_of_birth', 'fine', 'email')

class BookForm(forms.ModelForm):
    isbn = forms.CharField(
        label='ISBN код книги',
        widget=forms.TextInput(
            attrs={'class': 'input-1', 'placeholder': 'Введите ISBN код книги'}
        )
    )

    title = forms.CharField(
        label='Название книги',
        widget=forms.TextInput(
            attrs={'class': 'input-1', 'placeholder': 'Введите название книги'}
        )
    )

    publication_date = forms.DateField(
        label='Дата публикации книги',
        widget=forms.DateInput(
            attrs={'class': 'datepicker-input', 'placeholder': 'Дата публикации книги', 'id': 'datetimepicker'}
        )
    )

    cost = forms.IntegerField(
        label='Цена',
        widget=forms.NumberInput(
            attrs={'class': 'input-1', 'placeholder': 'Введите цену книги'}
        )
    )

    class Meta:
        model = Book
        fields = ('isbn', 'title', 'publication_date', 'author', 'cost')

class CardItemForm(forms.ModelForm):
        model = CardItem
        fields = ('book', 'given_date', 'returned_date', 'status', 'client')