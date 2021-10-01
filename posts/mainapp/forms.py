from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from bootstrap_datepicker_plus import DateTimePickerInput

from .models import Comment


class DateInput(forms.DateTimeInput):
    input_type = 'date'


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('text', 'delay',)
        widgets = {'delay': DateTimePickerInput()}


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Login', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


class SignInUserForm(AuthenticationForm):
    username = forms.CharField(label='Login')
    password = forms.CharField(label='Password')